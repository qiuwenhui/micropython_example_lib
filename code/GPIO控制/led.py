# **************************************************************************** #
#                                                                              #
#                                                         ::::::::             #
#    led.py   for micropython                                          :+:    :+:             #
#    通过gpio 控制led 灯                                                 +:+                     #
#    By: anonymous <anonymous@student.codam.nl>       +#+                      #
#                                                    +#+                       #
#    Created: 2019/04/22 10:19:39 by anonymous      #+#    #+#                 #
#    Updated: 2019/04/22 10:19:39 by anonymous     ########   odam.nl          #
#                                                                              #
# **************************************************************************** #
import machine
p=machine.Pin(2,Pin.OUT)
p.off()#关
p.on()#开
p.value(0)#设置p输出为0
p.value(1)#设置p输出1