# IParser: Industrial Strength Dependency Parser

Yet another multilingual dependency parser, integrated with tokenizer, part-of-speech tagger and visualization tool. IParser can parse raw sentence to dependency tree in CoNLL format, and is able to visualize trees in your browser. [See live demo!](http://iparser.hankcs.com/)

Currently, iparser is in a prototype state. It makes no warranty and may not be ready for practical usage.

## Install

```
pip3 install iparser --process-dependency-links
```

## Quick Start

### CLI

#### Interactive Shell

You can play with IParser in an interactive mode:

```
$ iparser parse
I looove iparser!
1	I       _	_	PRP	_	2	nsubj	_	_
2	looove  _	_	VBP	_	0	root	_	_
3	iparser _	_	NN	_	2	dobj	_	_
4	!       _	_	.   _	2	punct
```
You type a sentence, hit enter, IParser will output its dependency tree.

- Use `iparser segment` or `iparser tag` for word segmentation or part-of-speech tagging
- Some models may take a while to load
- IParser is language-agnostic, we provide pre-trained models for both English and Chinese, shipped in the installation package. The default model is PTB (English), you can switch to CTB (Chinese) via appending `--language cn`
- Append `--help` to see the detail manual

#### Pipeline

```
$ iparser segment <<< '商品和服务'        
商品 和 服务

$ iparser tag <<< 'I looove iparser!'   
I/PRP looove/VBP iparser/NN !/.

$ iparser parse <<< 'I looove iparser!' 
1	I       _	_	PRP	_	2	nsubj	_	_
2	looove  _	_	VBP	_	0	root	_	_
3	iparser _	_	NN	_	2	dobj	_	_
4	!       _	_	.   _	2	punct	_	_
```

- `iparser` is a compatible pipeline for standard I/O redirection. You can use `iparser` directly in terminal without writing codes.

### API

#### IParser

The all-in-one interface is provided by class `IParser`:

```
$ python3
>>> from iparser import *
>>> iparser = IParser(pos_config_file=PTB_POS, dep_config_file=PTB_DEP)
>>> print(iparser.tag('I looove iparser!'))
[('I', 'PRP'), ('looove', 'VBP'), ('iparser', 'NN'), ('!', '.')]
>>> print(iparser.parse('I looove iparser!'))
1	I	_	_	PRP	_	2	nsubj	_	_
2	looove	_	_	VBP	_	0	root	_	_
3	iparser	_	_	NN	_	2	dobj	_	_
4	!	_	_	.	_	2	punct	_	_
```

You can load models trained on different corpora to support multilingual:

```
>>> iparser = IParser(seg_config_file=CTB_SEG, pos_config_file=CTB_POS, dep_config_file=CTB_DEP)
>>> print(iparser.parse('我爱依存分析！'))
1	我	_	_	PN	_	2	nsubj	_	_
2	爱	_	_	VV	_	0	root	_	_
3	依存	_	_	VV	_	2	ccomp	_	_
4	分析	_	_	VV	_	3	comod	_	_
5	！	_	_	PU	_	2	punct	_	_
```

If you only want to perform an intermediate step, you can checkout the following APIs.

#### Word Segmentation

```
>>> segmenter = Segmenter(CTB_SEG).load()
>>> segmenter.segment('下雨天地面积水')
['下雨天', '地面', '积水']
```

- Notice that you need to call `load` to indicate that you want to load a pre-trained model, not to prepare an empty model for training.

#### Part-of-Speech Tagging

```
>>> tagger = POSTagger(PTB_POS).load()
>>> tagger.tag('I looove languages'.split())
[('I', 'PRP'), ('looove', 'VBP'), ('languages', 'NNS')]
```

- `POSTagger` is not responsible for word segmentation. Do segmentation in advance or use `IParser` for convenience.

#### Dependency Parsing

```
>>> parser = DepParser(PTB_DEP).load()
>>> sentence = [('Is', 'VBZ'), ('this', 'DT'), ('the', 'DT'), ('future', 'NN'), ('of', 'IN'), ('chamber', 'NN'), ('music', 'NN'), ('?', '.')]
>>> print(parser.parse(sentence))
1	Is	_	_	VBZ	_	4	cop	_	_
2	this	_	_	DT	_	4	nsubj	_	_
3	the	_	_	DT	_	4	det	_	_
4	future	_	_	NN	_	0	root	_	_
5	of	_	_	IN	_	4	prep	_	_
6	chamber	_	_	NN	_	7	nn	_	_
7	music	_	_	NN	_	5	pobj	_	_
8	?	_	_	.	_	4	punct	_	_
```

- `DepParser` is neither responsible for segmentation nor tagging. 
- The input must be a list of tuples of word and tag.

### Server

```
$ iparser.server
usage: iparser.server [-h] [--port PORT]

A http server for IParser

optional arguments:
  -h, --help   show this help message and exit
  --port PORT
```

- The default URL is http://localhost:8666/
- You can check our live demo at http://iparser.hankcs.com/


## Train Models

IParser is designed to be language-agnostic, which means it has universal language support, only need to give some corpora of a desired language. 

### Corpus Format

The format is described here: https://github.com/hankcs/TreebankPreprocessing

### Configuration File

IParser employs configuration files to ensure the same network is created before and after serialization, in training phase and testing phase accordingly. This is important for research engineers who want to fine-tune those hyper parameters, or train new models on third language corpora. We provide well documented configuration template files, containing all configurable parameters for users to adjust. 

You can check out templates shipped with the `iparsermodels`, e.g.

```
python3
>>> from iparser import *
>>> PTB_DEP
'/usr/local/python3/lib/python3.6/site-packages/iparsermodels/ptb/dep/config.ini'
```

### CLI

The CLI is not only capable for prediction, but also can perform training. Only requires a configuration file.

```
$ iparser segment --help
usage: iparser segment [-h] [--config CONFIG] [--action ACTION]

optional arguments:
  -h, --help       show this help message and exit
  --config CONFIG  path to config file
  --action ACTION  Which action (train, test, predict)?
```

- `--action train` is what you are looking for.

### API

The training APIs can be found in `tests/train_parser.py` etc.

## Performance

![tag](http://wx1.sinaimg.cn/large/006Fmjmcly1fpgvl4ijsoj31kw07zgn9.jpg)

![dep](http://wx3.sinaimg.cn/large/006Fmjmcly1fpgvlqpigpj31kw0bmjtt.jpg)

The character model seems to be useless for English and Chinese, so it is disabled by default.

## Acknowledgments

- Bi-LSTM-CRF implementation modified from a Dynet-1.x version by [rguthrie3](https://github.com/rguthrie3/BiLSTM-CRF).
- BiAffine implementation extended from [jcyk](https://github.com/jcyk/Dynet-Biaffine-dependency-parser), added a subword LSTM layer with attention, as introduced in [Stanford's Graph-based Neural Dependency Parser at the CoNLL 2017 Shared Task](https://web.stanford.edu/~tdozat/files/TDozat-CoNLL2017-Paper.pdf).
- Visualization part is adopted from [Annodoc](https://github.com/spyysalo/annodoc), an annotation documentation support system which is used as a wrapper of BRAT.


