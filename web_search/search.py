"""Web Search Module

This module provides the core functionality for performing web searches.
"""

import requests
from typing import List, Dict, Optional

from web_search.searcher.bing import search_bing
from web_search.searcher.baidu import search_baidu

class WebSearch:
    """Web Search class that provides methods for performing web searches."""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the WebSearch instance.
        
        Args:
            api_key (str, optional): API key for the search service.
        """
        self.api_key = api_key
    
    def search(self, query: str, engines: list=None, cookie: str="", num_results: int = 10) -> List[Dict]:
        """Perform a web search.
        
        Args:
            query (str): The search query.
            engines (list): ['baidu', 'bing'].
            cookie (str): Cookie for the search service.
            num_results (int): Number of results to return.
            
        Returns:
            List[Dict]: List of search results, each containing 'title', 'link', and 'snippet'.
        """
        # TODO: Implement actual search functionality
        # This is a placeholder that should be replaced with actual search implementation
        all_results = []
        if not engines:
            engines = ['baidu', 'bing']
        for engine in engines:
            if engine == 'baidu':
                results = search_baidu(query)
            elif engine == 'bing':
                results = search_bing(query, cookie=cookie)
            else:
                continue
            all_results.extend(results)
        # results = search_baidu(query)
        for result in all_results:
            print(f"logo：{result['logo']}")
            print(f"网站：{result['website']}")
            print(f"标题：{result['title']}")
            print(f"链接：{result['link']}")
            print(f"摘要：{result['detail']}")
            print(f"日期：{result['date']}")
            print("-" * 50)
        return results
    
    def get_suggestions(self, query: str) -> List[str]:
        """Get search suggestions for a query.
        
        Args:
            query (str): The partial search query.
            
        Returns:
            List[str]: List of search suggestions.
        """
        # TODO: Implement search suggestions functionality
        return [f"{query} example suggestion"]

cookie = "MUID=07773052BF4A6B1611C325CDBE356A9F; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=A21D973E441441AEB319339E0471D2F3&dmnchg=1; MUIDB=07773052BF4A6B1611C325CDBE356A9F; ANON=A=1095D6ABBD8DB83F1CAB3F07FFFFFFFF; MUIDV=NU=1; MMCASM=ID=920EF73B5C1E46DEBA1A4EA801A347A3; _tarLang=default=en; _TTSS_IN=hist=WyJlbiIsInpoLUhhbnMiLCJhdXRvLWRldGVjdCJd&isADRU=0; _TTSS_OUT=hist=WyJ6aC1IYW5zIiwiZW4iXQ==; SRCHUSR=DOB=20250226&T=1743505016000&DS=1; _UR=QS=0&TQS=0&Pn=0; BFBUSR=BFBHP=0; _Rwho=u=d&ts=2025-05-24; _EDGE_S=SID=1A9CFA2607E868B82D38EFD006C66943&ui=zh-cn; imgv=lodlg=2&gts=20250524; USRLOC=HS=1&ELOC=LAT=39.91499710083008|LON=116.42433166503906|N=%E4%B8%9C%E5%9F%8E%E5%8C%BA%EF%BC%8C%E5%8C%97%E4%BA%AC%E5%B8%82|ELT=2|&CLOC=LAT=39.91499540687248|LON=116.4243325215717|A=733.4464586120832|TS=250524050327|SRC=W&BID=MjUwNTI0MTMwMzI3X2FmOTg4MTczNDVlOTFlOTZlZjVjYzdlYTNiY2MyMzc0NGZlZjIxZmEzMDU1MmJkMTI3YmEzZjI1NDc3NDlmYmQ=; BFPRResults=FirstPageUrls=9B307DBC41DA547A6AF40858E18E10F2%2C050B9F35BFE30A43F1C68AF485CA9280%2CFA0161890975C84CB4CC39E5DCB00134%2C0D62B3D8A6886BBEF00D61658E34E7C1%2C89CDCD26797DDA6430CB7DF6E721A76D%2C74C9FA084D76A031769A024C1EDD0137%2CB255AC44F4C8DBE1BBE92515EF8F428D%2C97E82A01C017F24965CC29E4A18DD7CA%2C55121F4C6F0D4541632995081BC3646C%2C58E912346767210FA52DEB68EEF18C97&FPIG=99654EEA1B6649D7A3230D00B7E5E4A9; ipv6=hit=1748074767583&t=4; _SS=SID=1A9CFA2607E868B82D38EFD006C66943&PC=PCMEDGEDP&R=3139&RB=3139&GB=0&RG=0&RP=3139; _HPVN=CS=eyJQbiI6eyJDbiI6MywiU3QiOjAsIlFzIjowLCJQcm9kIjoiUCJ9LCJTYyI6eyJDbiI6MywiU3QiOjAsIlFzIjowLCJQcm9kIjoiSCJ9LCJReiI6eyJDbiI6MywiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNS0wNS0yNFQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjo1LCJUb2JuIjowfQ==; _C_ETH=1; GC=JRDNAFKk6hfOdbdO8i4Hm2RnUEtN-PyFppLAoCpfhqLbUv6p2u2Bf2tIdPnJYIhjwcTMvyctizElfkmr_DAwBw; _RwBf=r=0&ilt=2&ihpd=0&ispd=2&rc=3139&rb=3139&gb=2025w17_c&rg=0&pc=3139&mtu=0&rbb=0.0&g=&cid=0&clo=0&v=6&l=2025-05-24T07:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=-62135539200&rwflt=1682205401&rwaul2=0&o=16&p=bingcopilotwaitlist&c=MY00IA&t=7477&s=2023-04-05T00:28:50.5066749+00:00&ts=2025-05-24T07:21:25.0930041+00:00&rwred=0&wls=2&wlb=0&wle=0&ccp=2&cpt=0&lka=0&lkt=0&aad=0&TH=&mta=0&e=M7h0WeGO7k_bntc-EM2rw9lkG9kepkZjYEuKSXwSL-1QwS-9e2yMKoatmhIdJB0AaDHLLWwVaWy8avy_JhucyQ&A=1095D6ABBD8DB83F1CAB3F07FFFFFFFF; .MSA.Auth=CfDJ8Inh5QCoSQBNls38F2rbEpReUfWB05duuUyqXIAuG2ZCNzmTlXL2kEBWucwFSHBvLgphktxr-UXZ2R5qvrjc5RZH-WYm4CZNXjIdwRJaLsXSvM6gdsFAVPSYrExzAc0vz6lDUMoiuVbaGSXJMsPy3Dio7ZpSDs4WW-yTTLc_G7e9_T5u9HjUQ9dBBU4iQ_5xCpuCBHnxnGEIeS41gMRqTxA8uKb-OuOP7jPIyvg9rfVRXE8MIbu5UmvuuW-peDnqy57zVNBuhO3fZ6qH-Txl_HcJS6Q2ZNSXYgWuGnWwk0HPGsQS8JqJ9WjRS03mvsUCgiy3JfE4d8BJ6eAYTQOjNECLtN5snqaeLficDK0X201Q; SNRHOP=I=&TS=; _U=1fO3wCcKRNreILkkjwlQ_T7jr0cYhxl_oSBHamRAZEWGf1EoP7FppWV8GFuL-7cpMQfhlIhKkVLLtvNe50iD8tB12BTo3Astez6VHQ0_NeahxebAcyX5m4hyjbvzty4IVbIDRgrGrUi282Hi6yL15T2IbwYWMkypjFJfpJNMC0AVHMBwj_8Y6DxFPJxBEQi9Fq0wIBYsHMTwSs1u0A70DEA; SRCHHPGUSR=SRCHLANG=zh-Hans&PV=19.0.0&DM=0&BRW=XW&BRH=S&CW=1699&CH=515&SCW=1684&SCH=2560&DPR=1.5&UTC=480&EXLTT=31&HV=1748071285&HVE=CfDJ8Inh5QCoSQBNls38F2rbEpRFSWschHOg28MX-OmrkTU3JbXV9VFVVxqy9OgOClBnO1VPJOclWo2lOXZ7zF7DD7XK2JZbE99NzWRpfqbZelP0nfpBrb7IriSWAqazHwZk6g6MkiceKrNbIxJM_-ymMqmpyTOOpCliuNJnZb9O5mpVevdwHhk1BD_Mt_nm6k3usQ&BZA=0&PRVCW=1699&PRVCH=406&AV=14&ADV=14&RB=0&MB=0&DMREF=0&WTS=63883584329&PREFCOL=0; WLS=C=c83c7a19ced44162&N="

ws = WebSearch()
ws.search("2024年高考报名时间", cookie=cookie)
# print(results)