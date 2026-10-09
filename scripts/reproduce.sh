#!/bin/bash

set -e

echo "Step 1: train model"

python src/train.py \
    --config configs/base.yaml

echo "Step 2: evaluate model"

python src/eval.py \
    --config configs/base.yaml \
    --checkpoint checkpoints/model.pt
