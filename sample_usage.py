from RVCAudioConverter import RVCAudioConverter

MODEL_PTH_PATH = "assets/custom_models/spongebob/model.pth"
MODEL_INDEX_PATH = "assets/custom_models/spongebob/model.index"
output_format = "ogg" #"wav"
# for batch folder processing
INPUT_FOLDER_PATH = "input_folder/"
OUTPUT_FOLDER_PATH = "output_folder/"

rvc = RVCAudioConverter(MODEL_PTH_PATH, MODEL_INDEX_PATH, skip_first_setup=False, skip_spongebob_model=False)
rvc.parse_batch_audio(INPUT_FOLDER_PATH, OUTPUT_FOLDER_PATH, output_format=output_format)

# for single file procesing
INPUT_FILE_PATH = "input_folder/in.ogg"
OUTPUT_FILE_PATH = "output_folder/out.ogg"

rvc.parse_single_audio(INPUT_FILE_PATH, OUTPUT_FILE_PATH, output_format=output_format)