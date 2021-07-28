# lrs2_alignment

To align lrs2 dataset using montrel-forced-alignment to phoneme,

we need the `.wav` file (if no sox installed) or `.mp4` file with the corresponding `.txt` file.

Since the original .txt file contains not only the transcribed words,

we first simplify the .txt file with `python simplify.py`.

If no sox installed, all the .mp4 files need to be converted to .wav files by `python convert.py`,

since it can only process on the .wav files.

After installing montreal-forced-alignment (http://montreal-forced-aligner.readthedocs.io/),

we can generate the corresponding alignment file with `python align.py`.

Then rename the generated file and move it to the original directory with `python rename.py`.
