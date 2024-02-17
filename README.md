# TDSR Plugins

This repo works with [TDSR](https://github.com/tspivey/tdsr) to allow for some easier terminal reading of certain commands output.

## Setup

Clone this repo into TDSR (the below example assumes you have tdsr in your home directory)

`git clone https://github.com/hbk619/tdsr-plugins ~/tdsr/plugins/hbk619`

### Pytest

If you would like to use pytest and have feedback as "3 errors. Module not found. 
Code is import blah" configure TDSR in the plugins section as below

```
hbk619.pytest_parser = p
```

If you would like to make parsing slightly faster and have a consistent command to run pytest
you can add it under the commands section

```
hbk619.pytest_parser = pytest -x
```


### Git status

If you would like to use git and have feedback for the status command indicating what files are staged e.g.
"new file path/to/file.txt modified another/file.py" configure TDSR in the plugins section as below

```
hbk619.git_status = p
```

If you would like to make parsing slightly faster and have a consistent command to run git status
you can add it under the commands section

```
hbk619.git_status = git status
```

### Tab auto complete

If you would like to hear the items shown in the terminal when you press tab to auto complete a path, along
with what is selected you can add the below to the commands section, provided you are using a zsh terminal

```
hbk619.tabbing = ^(\(.*\))?➜\s{2}.+✗?
```

### Maven

If you ue maven would like to hear test results as "3 passed, 1 failed. Got thing. Expected something else.
Test is test thing line 21" or Java compilation errors as "file name.java line 2 column 2 expected ;" add the below to the commands section

```
hbk619.maven = mvn
```

### Custom Voice

If you would like to hear your pytest errors in a voice from ElevenLabs you can use the custom_voice plugin.
You will need to install the elevenlabs module which if you installed TDSR requirements as a user you can do with:

```
pip install -U elevenlabs==0.2.27
```

The way you start TDSR will need to change as you will need an environment variable called VOICE_ID and if the voice is private you will also need one called ELEVENLABS_API

Start TDSR with the below, replacing <your value> with your actual value

```
VOICE_ID=<your value> ELEVENLABS_API=<your value> ~/tdsr/tdsr
```

Then configure TDSR in the plugins section as below

```
hbk619.custom_voice = a
```

If you would like to make parsing slightly faster and have a consistent command to run pytest
you can add it under the commands section

```
hbk619.custom_voice = pytest -x
```

At the moment it's just pytest it works with, I'm working on a way to say any command in a voice from Elevenlabs.


## Custom voice speech server (experimental)
You can use the ElevenLabs speech server in this repo too, however it will use your quota very quickly so if you have a limited
amount of api requests be careful! It's also experimental and a bit buggy and there is no way to stop the audio once it starts, you have been warned!

You will need to install the elevenlabs module which if you installed TDSR requirements as a user you can do with:

```
pip install -U elevenlabs==0.2.27
```

To use the speech server change the way you start TDSR as below, replacing <your value> with your actual value

```
VOICE_ID=<your value> ELEVENLABS_API=<your value> ~/tdsr/tdsr --speech-server ~/tdsr/plugin/hbk619/elevenlabs-server.py
```

If you would like to see what is being sent to ElevenLabs you can enable debugging with an environment variable as below. This will create the 
log file `~/tdsr/plugins/hbk619/hbk619-plugin.log`

```
HBK619_DEBUG=true VOICE_ID=<your value> ELEVENLABS_API=<your value> ~/tdsr/tdsr --speech-server ~/tdsr/plugins/hbk619/elevenlabs-server.py
```