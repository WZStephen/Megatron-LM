#!/usr/bin/env bash

python /home/zhaowc/Megatron-LM/tools/preprocess_data.py \
  --input /home/zhaowc/Megatron-LM/_datasets/openwebtext_small/raw_data.json \
  --tokenizer-type GPT2BPETokenizer \
  --vocab-file /home/zhaowc/Megatron-LM/_datasets/gpt_vocab.json \
  --merge-file /home/zhaowc/Megatron-LM/_datasets/gpt_merges.txt \
  --output-prefix /home/zhaowc/Megatron-LM/_datasets/openwebtext_small \
  --workers 8 \
  --chunk-size 1000
