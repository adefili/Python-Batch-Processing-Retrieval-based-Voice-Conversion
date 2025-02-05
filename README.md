## Description
realistic speech-to-speech transformations using Retrieval-based-Voice-Conversion in pyhon 

## WIP
- simple training

## Feature
- semplified setup
- easy batch processing
- easy models download
- from any audio format to any audio format
- use pip instead of poetry

## Requirements
working with `python 3.10.14`

## Installation
clone the repositories

create a python env

ensure `pip 24.0` is installed. pip 25.x or higher will break

pip install -r requirements.txt

install required packages using "pip install git+https://github.com/RVC-Project/Retrieval-based-Voice-Conversion.git@develop"

`rvc` folder is alredy attached in the repositories. alternatively you get it from "https://github.com/RVC-Project/Retrieval-based-Voice-Conversion/tree/develop/rvc"

to permit unsafe pickles loading and avoid errors, i had to do the following changes inside `rvc/modules/vc/modules.py`(the one in the repository is alredy changed) and `{your python env or python installation path}/Lib/site-packages/fairseq/checkpoint_utils.py`

from `torch.load(...)` -> `torch.load(..., weights_only=False)`

# Running
the scripts manage to download all needed models plus a custom spongebob model to do a quick "hello world"

the class initialization will download by default all needed models.

```python
from RVCAudioConverter import RVCAudioConverter

MODEL_PTH_PATH = "assets/custom_models/spongebob/model.pth"
MODEL_INDEX_PATH = "assets/custom_models/spongebob/model.index"
output_format = "ogg" #"wav"
# for batch folder processing
INPUT_FOLDER_PATH = "input_folder/"
OUTPUT_FOLDER_PATH = "output_folder/"

rvc = RVCAudioConverter(MODEL_PTH_PATH, MODEL_INDEX_PATH, skip_first_setup=False, skip_spongebob_model=False)
rvc.parse_batch_audio(INPUT_FOLDER_PATH, OUTPUT_FOLDER_PATH, output_format=output_format)
```

check sample_usage.py for a quick overview


