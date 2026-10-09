#!/bin/bash

set -e

python src/eval.py \
    --config configs/base.yaml \
    --checkpoint checkpoints/model.pt
