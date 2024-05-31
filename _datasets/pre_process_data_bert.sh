#!/usr/bin/env bash

python /home/zhaowc/Megatron-DeepSpeed/tools/preprocess_data.py \
  --input /home/zhaowc/Megatron-LM/_datasets/openwebtext_small/raw_data.json \
  --output-prefix /home/zhaowc/Megatron-LM/_datasets/my-bert \
  --vocab-file /home/zhaowc/Megatron-LM/_datasets/bert_vocab.txt \
  --tokenizer-type BertWordPieceLowerCase \
  --split-sentences \
  --workers 8