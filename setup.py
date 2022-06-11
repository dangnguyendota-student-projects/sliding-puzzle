from cx_Freeze import setup,Executable

executables=[Executable('Game.py')]
setup(name="my game",
      options={"build_exe":{"packages":["pygame"],
                                      "include_files":[]}},
      executables=executables)