# -*- coding: utf-8 -*-
# @Date    : 2016-10-21 
# @Author  : Bruce (hanyan_007@139.com)
# @Link    : https://github.com/hanyan007/python_home

import optparse
import  sys
import urllib2


usage="""%prog <ip>
Samples:
    %prog 8.8.8.8 """

#from optparse import OptionParser  
def main():
    parser = optparse.OptionParser(usage = usage)

    (options, arguments) = parser.parse_args()

    if len(sys.argv) < 2:
        parser.print_usage()
        return -1

    ip = arguments.pop(0)
	
    try:

	res = urllib2.urlopen("http://ip.taobao.com//service/getIpInfo.php?ip="+ip)
	a = res.read()
	zidian = eval(a)	
#	print zidian
	#print zidian.decode("unicode_escape")
#	print ip
	country=zidian['data']['country'].decode("unicode_escape")
	area=zidian['data']['area'].decode("unicode_escape")
	region=zidian['data']['region'].decode("unicode_escape")
	city=zidian['data']['city'].decode("unicode_escape")
	isp=zidian['data']['isp'].decode("unicode_escape")	
	ip=zidian['data']['ip']
	
	print ip,isp,city,region,area,country



    except Exception, e:
        print "ThreatBook returned a non correct response."

if __name__ == "__main__":
    main()




