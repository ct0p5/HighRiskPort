#!usr/bin/env python
# coding: utf-8

import argparse
import os

'''
利用nmap扫描特定的敏感端口

'''


def nmapscan(host):
    port_list = ' -p 21,22,23,80,81,389,443,512,873,1433,1521,2375,2601,2604,3128,3306,3389,4440,6082,6379,7001,8000,8008,8080,8081,8090,8099,8088,8888,9000,9060,9080,9090,9200,11211,27017,28017,50000,50070,U:161'
    commend = 'nmap -sT -sV ' + str(host) + port_list + ' --max-hostgroup 10 --max-parallelism 10 --max-rtt-timeout 1000ms --host-timeout 800s --max-scan-delay 2000ms'
    os.system(commend)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='nmap High-risk ports scan')
    parser.add_argument('--host', dest='host', required=True, help='Target host(s)')
    args = parser.parse_args()
    nmapscan(args.host)
