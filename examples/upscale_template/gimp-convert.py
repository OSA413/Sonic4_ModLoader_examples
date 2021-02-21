import subprocess, os

with open("gimp-convert.bat", "r") as f:
    main_script = f.read()

with open("gimp-convert.fu", "r") as f:
    script = f.read().replace("\n", " ").replace("\"", "\\\"")

subprocess.run(main_script + " \"" + script + "\" --batch \"(gimp-quit 1)\"",
    cwd = os.getcwd(),
    shell = True)
