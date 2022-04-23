from termcolor import cprint
from time import sleep

class TrafficLight:
  __color = ""

  def running(self, f_color, s_color, t_color):
    if f_color != "red":
      print("First color of trafficlight must be \033[31m{}".format("RED"))
      return False
    elif s_color != "yellow":
      print("First color of trafficlight must be \033[33m{}".format("YELLOW"))
      return False
    elif t_color != "green":
      print("First color of trafficlight must be \033[32m{}".format("GREEN"))
      return False
    conf_list = {f_color: 7, s_color: 2, t_color: 10}
    for i in conf_list.keys():
      self.__color = i
      cprint(chr(9679), self.__color)
      sleep(conf_list.get(i))

a = TrafficLight()
a.running("red", "yellow", "green")