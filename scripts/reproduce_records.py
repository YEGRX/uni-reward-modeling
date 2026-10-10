#!/usr/bin/env python3
"""Verify archived records and reconstruct published tables; no model execution."""
import argparse
import csv
import hashlib
import io
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def local_path(name):
    path = (ROOT / name).resolve()
    require(path.is_relative_to(ROOT), 'Path outside repository: ' + name)
    return path


def read_json(name):
    return json.loads(local_path(name).read_text(encoding='utf-8'))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_docs():
    log = local_path('docs/experiment_log.md').read_text(encoding='utf-8')
    entries = re.split(r'(?=^## \d{4}-\d{2}-\d{2} — )', log, flags=re.M)[1:]
    require(len(entries) == 87, 'Expected 87 log entries')
    for entry in entries:
        for field in ('Experiment', 'Config', 'Result', 'Conclusion', 'Next'):
            require('**' + field + ':**' in entry, 'Missing log field: ' + field)
    pages = [ROOT / 'README.md', ROOT / 'TODO.md', *ROOT.glob('docs/**/*.md')]
    for page in pages:
        body = re.sub(r'```.*?```', '', page.read_text(encoding='utf-8'), flags=re.S)
        for url in re.findall(r'!?\[[^\]\n]*\]\(([^\)\n]+)\)', body):
            if url.startswith(('https://', 'http://', '#', 'mailto:')):
                continue
            target = (page.parent / url.split('#')[0].strip('<>')).resolve()
            require(target.is_relative_to(ROOT) and target.exists(), 'Broken internal link: ' + str(page.relative_to(ROOT)) + ': ' + url)


def csv_text(rows, fields):
    out = io.StringIO(newline='')
    writer = csv.DictWriter(out, fieldnames=fields, lineterminator='\n')
    writer.writeheader()
    for row in rows:
        writer.writerow({k: json.dumps(row[k], ensure_ascii=False) if isinstance(row[k], (list, dict)) else row[k] for k in fields})
    return out.getvalue()


def verify_sources():
    assets = read_json('results/repository_assets.json')
    require(len({a['path'] for a in assets}) == len(assets), 'Duplicate assets')
    for asset in assets:
        p = local_path(asset['path'])
        require(p.is_file() and p.stat().st_size == asset['bytes'], 'Asset size mismatch: ' + asset['path'])
        require(sha(p) == asset['sha256'], 'Asset SHA mismatch: ' + asset['path'])
    manifest = read_json('results/source_manifest.json')['experiments']
    catalog = read_json('results/experiment_catalog.json')
    require(len(catalog) == len(manifest) == 87, 'Expected 87 archived records')
    by_id = {row['id']: row for row in manifest}
    require(len(by_id) == 87, 'Duplicate source IDs')
    require(len({row['experiment_id'] for row in catalog}) == 87, 'Duplicate catalog IDs')
    for record in catalog:
        source = by_id[record['experiment_id']]
        for key in ('record', 'config', 'source'):
            require(local_path(record[key]).is_file(), 'Missing ' + record[key])
        require(sha(local_path(source['snapshot_file'])) == source['snapshot_sha256'], 'Snapshot mismatch')
        require(record['category'] == source['category'], 'Source category mismatch')
        require(read_json(record['config'])['experiment_id'] == record['experiment_id'], 'Config ID mismatch')
        primary = source['primary_report']
        if primary:
            require(sha(local_path(primary['file'])) == primary['sha256'], 'Primary report mismatch')
    require(sum(s['primary_report'] is not None for s in manifest) == 17, 'Expected 17 final reports')
    return len(assets)


def tables():
    main = read_json('results/evidence/q32-forward/MAIN8_RESULTS.json')
    val = read_json('results/evidence/q32-forward/VAL_RESULTS.json')
    decision = read_json('results/evidence/q32-forward/OVERALL_DECISION.json')
    fd = read_json('results/evidence/q32-stop/FD_CHECK.json')
    require(main['counts']['MAIN8_dina'] == 6912, 'Pair-specific MAIN8 must be 6912')
    require(val['counts']['VAL_dina'] == 768, 'VAL must be 768')
    require(val['human_Accuracy'] is None, 'VAL has no human Accuracy')
    require(decision['status'] == 'MAIN8_TRADEOFF_OR_DETERIORATION', 'Stop classification changed')
    require(fd['passed'] is False and fd['ratio'] > decision['old_FD_threshold'], 'Original FD failure changed')
    require(decision['derivative_model_rehabilitated'] is False, 'Derivative qualification cannot be restored')
    for field in ('new_small_fits', 'new_training', 'new_backward', 'new_FD', 'new_VAE', 'new_Projector'):
        require(decision[field] == 0, 'Unexpected new work: ' + field)
    require(decision['MAIN8_new_results'] == main, 'Decision/result mismatch')
    require(len(main['bootstrap']['groups']) == 8, 'Fixed MAIN8 group count changed')
    require(main['primary_effects']['r_G']['classification'] == 'DETERIORATION_SUPPORTED', 'r_G classification changed')
    require(main['primary_effects']['r_G']['adjusted_CI'][1] < 0, 'r_G interval mismatch')
    require(main['primary_effects']['dAcc']['adjusted_CI'][0] < 0 < main['primary_effects']['dAcc']['adjusted_CI'][1], 'Accuracy uncertainty changed')
    rows = [{'method': name, **metrics} for name, metrics in main['methods'].items()]
    fields = ['method', *main['methods']['N_NATIVE'].keys()]
    effects = [{'effect': name, 'point': effect['point'], 'CI95': effect['CI95'], 'adjusted_CI': effect['adjusted_CI'], 'classification': effect['classification']} for name, effect in main['primary_effects'].items()]
    val_fields = ['method', 'centered_risk', 'risk_CI95', 'raw_score_MSE', 'common_offset_MSE', 'pair_margin_MSE', 'strict_G_agreement', 'strict_G_agreement_CI95', 'coordinate_MSE', 'relative_risk_reduction_vs_BASE', 'relative_reduction_CI95', 'paired_risk_reduction_vs_BASE_CI95']
    val_rows = [{'method': name, **metrics} for name, metrics in val['methods'].items()]
    keys = read_json('results/key_experiments.json')
    require(len(keys) == 17, 'Expected 17 key experiments')
    return {
        'results/tables/q32_main8.csv': csv_text(rows, fields),
        'results/tables/q32_main8_effects.csv': csv_text(effects, list(effects[0])),
        'results/tables/q32_val.csv': csv_text(val_rows, val_fields),
        'results/tables/experiment_summary.csv': csv_text(keys, list(keys[0])),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Read-only comparison against committed tables')
    args = parser.parse_args()
    count = verify_sources()
    verify_docs()
    rendered = tables()
    for name, content in rendered.items():
        path = local_path(name)
        if not args.check:
            with path.open('w', encoding='utf-8', newline='') as handle:
                handle.write(content)
        require(path.read_bytes() == content.encode('utf-8'), 'Table mismatch: ' + name)
    print('PASS: 87 records, 17 final reports, %d asset hashes, 4 published tables.' % count)
    print('Scope: documentation integrity and published-result table reconstruction; no new scientific replay or GPU calls.')


if __name__ == '__main__':
    main()
