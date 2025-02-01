# ModernBERT-code-tokenizer-insights
Comparing the tokenizers code abilities of ModernBERT, CodeBERT and BERT.


## Introduction  

[ModernBERT](https://arxiv.org/pdf/2412.13663)(2024) is the latest encoder-only model at the time of this repository's creation. The authors present it as a **Smarter, Better, Faster, and Longer** version of BERT, designed to improve performance across various NLP tasks.  

One of the key claims in the paper is that ModernBERT's tokenizer—built using an advanced BPE-based tokenization method—is inherently **"code-aware."** This claim stems from the fact that it was trained on a diverse mix of code and natural language data.  

The objective of this analysis is to rigorously evaluate ModernBERT's tokenizer in the context of **code tokenization** and compare its performance to that of [BERT](https://arxiv.org/pdf/1810.04805)(2018) and [CodeBERT](https://arxiv.org/pdf/2002.08155)(2020). Through various tests, this study aims to provide **quantifiable insights** into ModernBERT’s ability to handle programming constructs. Ultimately, this should help developers and researchers decide whether ModernBERT is the right choice for their applications, such as **retrieval-augmented generation (RAG)** and other **code-related tasks.**  

