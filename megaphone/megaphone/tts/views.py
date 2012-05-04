from django.http import HttpResponse
import subprocess
import os
import uuid


def tts(request):

    # Grab the string that we wish to encode to audio
    encode_string = request.REQUEST["string"]

    # Create a temporary file name for the audio file
    tmp_file = "/tmp/{0}.wav".format(str(uuid.uuid4()))

    cmd = ["say", "-o", tmp_file, "--file-format", "WAVE", encode_string, ]

    print " ".join(cmd)

    # Create a temporary audio file of the string
    subprocess.call(cmd)

    # Read the audio file into memory
    audio_buffer = open(tmp_file).read()

    # Remove the tmp file
    os.remove(tmp_file)

    # Return the contents of the audio file via HTTP
    return HttpResponse(audio_buffer, mimetype='audio/wave')
