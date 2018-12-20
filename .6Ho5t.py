# Tool Name :- 6Hos5t
# Author :- H4N5vs
# Date :- 21/12/2018
# Powered By :- Aex Software's

import sys
import os
from modules.logo import exit
from modules.menu import ToolX

class chk(object):
  def chos(self):
    if "linux" in sys.platform:
      # Running Tool-X on linux ....
      pass
    elif "darwin" in sys.platform:
      pass
      # print("Maaf ini tidak support untuk Device yang kamu gunakan")
      ex()
    elif "win" in sys.platform:
      print("Maaf tidak dapat di gunakan di windows, coba Install Emulator support Termux semisal Bluestack dan lain..")
      ex()
    else:
      print("Jika alat yang saya bikin tidak dapat di gunakan  \'%s\' right now !!!" %sys.platform)

def Tool_X():
  try:
	chk().chos()
	ToolX()

  except KeyboardInterrupt:
	exit()
Tool_X()
