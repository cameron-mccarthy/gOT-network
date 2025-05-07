
#!/bin/bash

declare -A vendors=(
  ["veth0"]="00:00:0C" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth4"]="00:00:23" # ABB INDUSTRIAL SYSTEMS AB # Relevant to OT due to ABB INDUSTRIAL SYSTEMS AB's involvement in industrial or automation systems.
  ["veth7"]="00:00:3C" # AUSPEX SYSTEMS INC. # Relevant to OT due to AUSPEX SYSTEMS INC.'s involvement in industrial or automation systems.
  ["veth20"]="00:00:5F" # Sumitomo Electric Industries, Ltd # Relevant to OT due to Sumitomo Electric Industries, Ltd's involvement in industrial or automation systems.
  ["veth23"]="00:00:65" # Network General Corporation # Relevant to OT due to Network General Corporation's involvement in industrial or automation systems.
  ["veth24"]="00:00:68" # ROSEMOUNT CONTROLS # Relevant to OT due to ROSEMOUNT CONTROLS's involvement in industrial or automation systems.
  ["veth33"]="00:00:81" # Bay Networks # Relevant to OT due to Bay Networks's involvement in industrial or automation systems.
  ["veth34"]="00:00:8A" # DATAHOUSE INFORMATION SYSTEMS # Relevant to OT due to DATAHOUSE INFORMATION SYSTEMS's involvement in industrial or automation systems.
  ["veth38"]="00:00:A2" # Bay Networks # Relevant to OT due to Bay Networks's involvement in industrial or automation systems.
  ["veth39"]="00:00:A3" # NETWORK APPLICATION TECHNOLOGY # Relevant to OT due to NETWORK APPLICATION TECHNOLOGY's involvement in industrial or automation systems.
  ["veth42"]="00:00:A7" # NETWORK COMPUTING DEVICES INC. # Relevant to OT due to NETWORK COMPUTING DEVICES INC.'s involvement in industrial or automation systems.
  ["veth44"]="00:00:A9" # NETWORK SYSTEMS CORP. # Relevant to OT due to NETWORK SYSTEMS CORP.'s involvement in industrial or automation systems.
  ["veth51"]="00:00:BC" # Rockwell Automation # Relevant to OT due to Rockwell Automation's involvement in industrial or automation systems.
  ["veth55"]="00:00:D0" # DEVELCON ELECTRONICS LTD. # Relevant to OT due to DEVELCON ELECTRONICS LTD.'s involvement in industrial or automation systems.
  ["veth65"]="00:00:F6" # APPLIED MICROSYSTEMS CORP. # Relevant to OT due to APPLIED MICROSYSTEMS CORP.'s involvement in industrial or automation systems.
  ["veth74"]="00:05:A8" # WYLE ELECTRONICS # Relevant to OT due to WYLE ELECTRONICS's involvement in industrial or automation systems.
  ["veth76"]="00:06:7C" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth77"]="00:06:C1" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth79"]="00:08:00" # MULTITECH SYSTEMS, INC. # Relevant to OT due to MULTITECH SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth86"]="00:10:06" # Thales Contact Solutions Ltd. # Relevant to OT due to Thales Contact Solutions Ltd.'s involvement in industrial or automation systems.
  ["veth87"]="00:10:07" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth88"]="00:10:08" # VIENNA SYSTEMS CORPORATION # Relevant to OT due to VIENNA SYSTEMS CORPORATION's involvement in industrial or automation systems.
  ["veth91"]="00:10:0B" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth93"]="00:10:0D" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth95"]="00:10:0F" # INDUSTRIAL CPU SYSTEMS # Relevant to OT due to INDUSTRIAL CPU SYSTEMS's involvement in industrial or automation systems.
  ["veth97"]="00:10:11" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth98"]="00:10:12" # PROCESSOR SYSTEMS (I) PVT LTD # Relevant to OT due to PROCESSOR SYSTEMS (I) PVT LTD's involvement in industrial or automation systems.
  ["veth100"]="00:10:14" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth103"]="00:10:17" # Bosch Access Systems GmbH # Relevant to OT due to Bosch Access Systems GmbH's involvement in industrial or automation systems.
  ["veth105"]="00:10:19" # SIRONA DENTAL SYSTEMS GmbH & Co. KG # Relevant to OT due to SIRONA DENTAL SYSTEMS GmbH & Co. KG's involvement in industrial or automation systems.
  ["veth109"]="00:10:1D" # WINBOND ELECTRONICS CORP. # Relevant to OT due to WINBOND ELECTRONICS CORP.'s involvement in industrial or automation systems.
  ["veth110"]="00:10:1E" # MATSUSHITA ELECTRONIC INSTRUMENTS CORP. # Relevant to OT due to MATSUSHITA ELECTRONIC INSTRUMENTS CORP.'s involvement in industrial or automation systems.
  ["veth111"]="00:10:1F" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth113"]="00:10:21" # ENCANTO NETWORKS, INC. # Relevant to OT due to ENCANTO NETWORKS, INC.'s involvement in industrial or automation systems.
  ["veth115"]="00:10:23" # Network Equipment Technologies # Relevant to OT due to Network Equipment Technologies's involvement in industrial or automation systems.
  ["veth116"]="00:10:24" # NAGOYA ELECTRIC WORKS CO., LTD # Relevant to OT due to NAGOYA ELECTRIC WORKS CO., LTD's involvement in industrial or automation systems.
  ["veth118"]="00:10:26" # ACCELERATED NETWORKS, INC. # Relevant to OT due to ACCELERATED NETWORKS, INC.'s involvement in industrial or automation systems.
  ["veth121"]="00:10:29" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth122"]="00:10:2A" # ZF MICROSYSTEMS, INC. # Relevant to OT due to ZF MICROSYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth123"]="00:10:2B" # UMAX DATA SYSTEMS, INC. # Relevant to OT due to UMAX DATA SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth124"]="00:10:2C" # Lasat Networks A/S # Relevant to OT due to Lasat Networks A/S's involvement in industrial or automation systems.
  ["veth126"]="00:10:2E" # NETWORK SYSTEMS & TECHNOLOGIES PVT. LTD. # Relevant to OT due to NETWORK SYSTEMS & TECHNOLOGIES PVT. LTD.'s involvement in industrial or automation systems.
  ["veth127"]="00:10:2F" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth133"]="00:10:35" # Elitegroup Computer Systems Co.,Ltd. # Relevant to OT due to Elitegroup Computer Systems Co.,Ltd.'s involvement in industrial or automation systems.
  ["veth134"]="00:10:36" # INTER-TEL INTEGRATED SYSTEMS # Relevant to OT due to INTER-TEL INTEGRATED SYSTEMS's involvement in industrial or automation systems.
  ["veth137"]="00:10:39" # Vectron Systems AG # Relevant to OT due to Vectron Systems AG's involvement in industrial or automation systems.
  ["veth138"]="00:10:3A" # DIAMOND NETWORK TECH # Relevant to OT due to DIAMOND NETWORK TECH's involvement in industrial or automation systems.
  ["veth139"]="00:10:3B" # HIPPI NETWORKING FORUM # Relevant to OT due to HIPPI NETWORKING FORUM's involvement in industrial or automation systems.
  ["veth148"]="00:10:45" # Nortel Networks # Relevant to OT due to Nortel Networks's involvement in industrial or automation systems.
  ["veth151"]="00:10:48" # HTRC AUTOMATION, INC. # Relevant to OT due to HTRC AUTOMATION, INC.'s involvement in industrial or automation systems.
  ["veth163"]="00:10:55" # FUJITSU MICROELECTRONICS, INC. # Relevant to OT due to FUJITSU MICROELECTRONICS, INC.'s involvement in industrial or automation systems.
  ["veth172"]="00:10:5E" # Spirent plc, Service Assurance Broadband # Relevant to OT due to Spirent plc, Service Assurance Broadband's involvement in industrial or automation systems.
  ["veth173"]="00:10:5F" # ZODIAC DATA SYSTEMS # Relevant to OT due to ZODIAC DATA SYSTEMS's involvement in industrial or automation systems.
  ["veth174"]="00:10:60" # BILLIONTON SYSTEMS, INC. # Relevant to OT due to BILLIONTON SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth177"]="00:10:63" # STARGUIDE DIGITAL NETWORKS # Relevant to OT due to STARGUIDE DIGITAL NETWORKS's involvement in industrial or automation systems.
  ["veth180"]="00:10:66" # ADVANCED CONTROL SYSTEMS, INC. # Relevant to OT due to ADVANCED CONTROL SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth182"]="00:10:68" # COMOS TELECOM # Relevant to OT due to COMOS TELECOM's involvement in industrial or automation systems.
  ["veth185"]="00:10:6B" # SONUS NETWORKS, INC. # Relevant to OT due to SONUS NETWORKS, INC.'s involvement in industrial or automation systems.
  ["veth196"]="00:10:77" # SAF DRIVE SYSTEMS, LTD. # Relevant to OT due to SAF DRIVE SYSTEMS, LTD.'s involvement in industrial or automation systems.
  ["veth198"]="00:10:79" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth200"]="00:10:7B" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth204"]="00:10:7F" # CRESTRON ELECTRONICS, INC. # Relevant to OT due to CRESTRON ELECTRONICS, INC.'s involvement in industrial or automation systems.
  ["veth207"]="00:10:82" # JNA TELECOMMUNICATIONS LIMITED # Relevant to OT due to JNA TELECOMMUNICATIONS LIMITED's involvement in industrial or automation systems.
  ["veth212"]="00:10:87" # XSTREAMIS PLC # Relevant to OT due to XSTREAMIS PLC's involvement in industrial or automation systems.
  ["veth213"]="00:10:88" # AMERICAN NETWORKS INC. # Relevant to OT due to AMERICAN NETWORKS INC.'s involvement in industrial or automation systems.
  ["veth218"]="00:10:8D" # Johnson Controls, Inc. # Relevant to OT due to Johnson Controls, Inc.'s involvement in industrial or automation systems.
  ["veth220"]="00:10:8F" # RAPTOR SYSTEMS # Relevant to OT due to RAPTOR SYSTEMS's involvement in industrial or automation systems.
  ["veth224"]="00:10:94" # Performance Analysis Broadband, Spirent plc # Relevant to OT due to Performance Analysis Broadband, Spirent plc's involvement in industrial or automation systems.
  ["veth226"]="00:10:96" # TRACEWELL SYSTEMS, INC. # Relevant to OT due to TRACEWELL SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth227"]="00:10:97" # WinNet Metropolitan Communications Systems, Inc. # Relevant to OT due to WinNet Metropolitan Communications Systems, Inc.'s involvement in industrial or automation systems.
  ["veth233"]="00:10:9D" # CLARINET SYSTEMS, INC. # Relevant to OT due to CLARINET SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth241"]="00:10:A5" # OXFORD INSTRUMENTS # Relevant to OT due to OXFORD INSTRUMENTS's involvement in industrial or automation systems.
  ["veth242"]="00:10:A6" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth247"]="00:10:AB" # KOITO ELECTRIC INDUSTRIES, LTD. # Relevant to OT due to KOITO ELECTRIC INDUSTRIES, LTD.'s involvement in industrial or automation systems.
  ["veth250"]="00:10:AE" # SHINKO ELECTRIC INDUSTRIES CO. # Relevant to OT due to SHINKO ELECTRIC INDUSTRIES CO.'s involvement in industrial or automation systems.
  ["veth255"]="00:10:B4" # ATMOSPHERE NETWORKS # Relevant to OT due to ATMOSPHERE NETWORKS's involvement in industrial or automation systems.
  ["veth261"]="00:10:BA" # MARTINHO-DAVIS SYSTEMS, INC. # Relevant to OT due to MARTINHO-DAVIS SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth263"]="00:10:BC" # Aastra Telecom # Relevant to OT due to Aastra Telecom's involvement in industrial or automation systems.
  ["veth264"]="00:10:BD" # THE TELECOMMUNICATION TECHNOLOGY COMMITTEE (TTC) # Relevant to OT due to THE TELECOMMUNICATION TECHNOLOGY COMMITTEE (TTC)'s involvement in industrial or automation systems.
  ["veth265"]="00:10:BE" # MARCH NETWORKS CORPORATION # Relevant to OT due to MARCH NETWORKS CORPORATION's involvement in industrial or automation systems.
  ["veth268"]="00:10:C1" # OI ELECTRIC CO.,LTD # Relevant to OT due to OI ELECTRIC CO.,LTD's involvement in industrial or automation systems.
  ["veth270"]="00:10:C3" # CSI-CONTROL SYSTEMS # Relevant to OT due to CSI-CONTROL SYSTEMS's involvement in industrial or automation systems.
  ["veth273"]="00:10:C6" # Universal Global Scientific Industrial Co., Ltd. # Relevant to OT due to Universal Global Scientific Industrial Co., Ltd.'s involvement in industrial or automation systems.
  ["veth274"]="00:10:C7" # DATA TRANSMISSION NETWORK # Relevant to OT due to DATA TRANSMISSION NETWORK's involvement in industrial or automation systems.
  ["veth275"]="00:10:C8" # COMMUNICATIONS ELECTRONICS SECURITY GROUP # Relevant to OT due to COMMUNICATIONS ELECTRONICS SECURITY GROUP's involvement in industrial or automation systems.
  ["veth276"]="00:10:C9" # MITSUBISHI ELECTRONICS LOGISTIC SUPPORT CO. # Relevant to OT due to MITSUBISHI ELECTRONICS LOGISTIC SUPPORT CO.'s involvement in industrial or automation systems.
  ["veth277"]="00:10:CA" # Telco Systems, Inc. # Relevant to OT due to Telco Systems, Inc.'s involvement in industrial or automation systems.
  ["veth284"]="00:10:D1" # Top Layer Networks, Inc. # Relevant to OT due to Top Layer Networks, Inc.'s involvement in industrial or automation systems.
  ["veth294"]="00:10:DB" # Juniper Networks # Relevant to OT due to Juniper Networks's involvement in industrial or automation systems.
  ["veth305"]="00:10:E6" # APPLIED INTELLIGENT SYSTEMS, INC. # Relevant to OT due to APPLIED INTELLIGENT SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth310"]="00:10:EB" # SELSIUS SYSTEMS, INC. # Relevant to OT due to SELSIUS SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth320"]="00:10:F5" # AMHERST SYSTEMS, INC. # Relevant to OT due to AMHERST SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth321"]="00:10:F6" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth324"]="00:10:F9" # UNIQUE SYSTEMS, INC. # Relevant to OT due to UNIQUE SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth327"]="00:10:FC" # BROADBAND NETWORKS, INC. # Relevant to OT due to BROADBAND NETWORKS, INC.'s involvement in industrial or automation systems.
  ["veth330"]="00:10:FF" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth333"]="00:20:03" # PIXEL POWER LTD. # Relevant to OT due to PIXEL POWER LTD.'s involvement in industrial or automation systems.
  ["veth341"]="00:20:0B" # OCTAGON SYSTEMS CORP. # Relevant to OT due to OCTAGON SYSTEMS CORP.'s involvement in industrial or automation systems.
  ["veth342"]="00:20:0C" # ADASTRA SYSTEMS CORP. # Relevant to OT due to ADASTRA SYSTEMS CORP.'s involvement in industrial or automation systems.
  ["veth348"]="00:20:12" # CAMTRONICS MEDICAL SYSTEMS # Relevant to OT due to CAMTRONICS MEDICAL SYSTEMS's involvement in industrial or automation systems.
  ["veth352"]="00:20:16" # SHOWA ELECTRIC WIRE & CABLE CO # Relevant to OT due to SHOWA ELECTRIC WIRE & CABLE CO's involvement in industrial or automation systems.
  ["veth357"]="00:20:1B" # NORTHERN TELECOM/NETWORK # Relevant to OT due to NORTHERN TELECOM/NETWORK's involvement in industrial or automation systems.
  ["veth361"]="00:20:1F" # BEST POWER TECHNOLOGY, INC. # Relevant to OT due to BEST POWER TECHNOLOGY, INC.'s involvement in industrial or automation systems.
  ["veth367"]="00:20:25" # CONTROL TECHNOLOGY, INC. # Relevant to OT due to CONTROL TECHNOLOGY, INC.'s involvement in industrial or automation systems.
  ["veth368"]="00:20:26" # AMKLY SYSTEMS, INC. # Relevant to OT due to AMKLY SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth370"]="00:20:28" # WEST EGG SYSTEMS, INC. # Relevant to OT due to WEST EGG SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth371"]="00:20:29" # TELEPROCESSING PRODUCTS, INC. # Relevant to OT due to TELEPROCESSING PRODUCTS, INC.'s involvement in industrial or automation systems.
  ["veth372"]="00:20:2B" # ADVANCED TELECOMMUNICATIONS MODULES, LTD. # Relevant to OT due to ADVANCED TELECOMMUNICATIONS MODULES, LTD.'s involvement in industrial or automation systems.
  ["veth377"]="00:20:30" # ANALOG & DIGITAL SYSTEMS # Relevant to OT due to ANALOG & DIGITAL SYSTEMS's involvement in industrial or automation systems.
  ["veth381"]="00:20:34" # ROTEC INDUSTRIEAUTOMATION GMBH # Relevant to OT due to ROTEC INDUSTRIEAUTOMATION GMBH's involvement in industrial or automation systems.
  ["veth385"]="00:20:38" # VME MICROSYSTEMS INTERNATIONAL CORPORATION # Relevant to OT due to VME MICROSYSTEMS INTERNATIONAL CORPORATION's involvement in industrial or automation systems.
  ["veth390"]="00:20:3D" # Honeywell Environmental & Combustion Controls # Relevant to OT due to Honeywell Environmental & Combustion Controls's involvement in industrial or automation systems.
  ["veth396"]="00:20:45" # ION Networks, Inc. # Relevant to OT due to ION Networks, Inc.'s involvement in industrial or automation systems.
  ["veth404"]="00:20:4E" # NETWORK SECURITY SYSTEMS, INC. # Relevant to OT due to NETWORK SECURITY SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth408"]="00:20:52" # RAGULA SYSTEMS # Relevant to OT due to RAGULA SYSTEMS's involvement in industrial or automation systems.
  ["veth409"]="00:20:53" # HUNTSVILLE MICROSYSTEMS, INC. # Relevant to OT due to HUNTSVILLE MICROSYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth410"]="00:20:54" # Sycamore Networks # Relevant to OT due to Sycamore Networks's involvement in industrial or automation systems.
  ["veth418"]="00:20:5C" # InterNet Systems of Florida, Inc. # Relevant to OT due to InterNet Systems of Florida, Inc.'s involvement in industrial or automation systems.
  ["veth426"]="00:20:64" # PROTEC MICROSYSTEMS, INC. # Relevant to OT due to PROTEC MICROSYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth427"]="00:20:65" # SUPERNET NETWORKING INC. # Relevant to OT due to SUPERNET NETWORKING INC.'s involvement in industrial or automation systems.
  ["veth430"]="00:20:69" # ISDN SYSTEMS CORPORATION # Relevant to OT due to ISDN SYSTEMS CORPORATION's involvement in industrial or automation systems.
  ["veth440"]="00:20:73" # FUSION SYSTEMS CORPORATION # Relevant to OT due to FUSION SYSTEMS CORPORATION's involvement in industrial or automation systems.
  ["veth441"]="00:20:74" # SUNGWOON SYSTEMS # Relevant to OT due to SUNGWOON SYSTEMS's involvement in industrial or automation systems.
  ["veth444"]="00:20:77" # KARDIOS SYSTEMS CORP. # Relevant to OT due to KARDIOS SYSTEMS CORP.'s involvement in industrial or automation systems.
  ["veth454"]="00:20:81" # TITAN ELECTRONICS # Relevant to OT due to TITAN ELECTRONICS's involvement in industrial or automation systems.
  ["veth457"]="00:20:84" # OCE PRINTING SYSTEMS, GMBH # Relevant to OT due to OCE PRINTING SYSTEMS, GMBH's involvement in industrial or automation systems.
  ["veth459"]="00:20:86" # MICROTECH ELECTRONICS LIMITED # Relevant to OT due to MICROTECH ELECTRONICS LIMITED's involvement in industrial or automation systems.
  ["veth462"]="00:20:89" # T3PLUS NETWORKING, INC. # Relevant to OT due to T3PLUS NETWORKING, INC.'s involvement in industrial or automation systems.
  ["veth465"]="00:20:8C" # GALAXY NETWORKS, INC. # Relevant to OT due to GALAXY NETWORKS, INC.'s involvement in industrial or automation systems.
  ["veth468"]="00:20:8F" # ECI Telecom Ltd. # Relevant to OT due to ECI Telecom Ltd.'s involvement in industrial or automation systems.
  ["veth473"]="00:20:95" # RIVA ELECTRONICS # Relevant to OT due to RIVA ELECTRONICS's involvement in industrial or automation systems.
  ["veth476"]="00:20:99" # BON ELECTRIC CO., LTD. # Relevant to OT due to BON ELECTRIC CO., LTD.'s involvement in industrial or automation systems.
  ["veth480"]="00:20:9D" # LIPPERT AUTOMATIONSTECHNIK # Relevant to OT due to LIPPERT AUTOMATIONSTECHNIK's involvement in industrial or automation systems.
  ["veth482"]="00:20:9F" # MERCURY COMPUTER SYSTEMS, INC. # Relevant to OT due to MERCURY COMPUTER SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth485"]="00:20:A2" # GALCOM NETWORKING LTD. # Relevant to OT due to GALCOM NETWORKING LTD.'s involvement in industrial or automation systems.
  ["veth487"]="00:20:A4" # MULTIPOINT NETWORKS # Relevant to OT due to MULTIPOINT NETWORKS's involvement in industrial or automation systems.
  ["veth491"]="00:20:A9" # WHITE HORSE INDUSTRIAL # Relevant to OT due to WHITE HORSE INDUSTRIAL's involvement in industrial or automation systems.
  ["veth495"]="00:20:AD" # LINQ SYSTEMS # Relevant to OT due to LINQ SYSTEMS's involvement in industrial or automation systems.
  ["veth503"]="00:20:B5" # YASKAWA ELECTRIC CORPORATION # Relevant to OT due to YASKAWA ELECTRIC CORPORATION's involvement in industrial or automation systems.
  ["veth504"]="00:20:B6" # AGILE NETWORKS, INC. # Relevant to OT due to AGILE NETWORKS, INC.'s involvement in industrial or automation systems.
  ["veth510"]="00:20:BC" # Long Reach Networks Pty Ltd # Relevant to OT due to Long Reach Networks Pty Ltd's involvement in industrial or automation systems.
  ["veth513"]="00:20:BF" # AEHR TEST SYSTEMS # Relevant to OT due to AEHR TEST SYSTEMS's involvement in industrial or automation systems.
  ["veth514"]="00:20:C0" # PULSE ELECTRONICS, INC. # Relevant to OT due to PULSE ELECTRONICS, INC.'s involvement in industrial or automation systems.
  ["veth516"]="00:20:C2" # TEXAS MEMORY SYSTEMS, INC. # Relevant to OT due to TEXAS MEMORY SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth517"]="00:20:C3" # COUNTER SOLUTIONS LTD. # Relevant to OT due to COUNTER SOLUTIONS LTD.'s involvement in industrial or automation systems.
  ["veth524"]="00:20:CB" # PRETEC ELECTRONICS CORP. # Relevant to OT due to PRETEC ELECTRONICS CORP.'s involvement in industrial or automation systems.
  ["veth526"]="00:20:CD" # HYBRID NETWORKS, INC. # Relevant to OT due to HYBRID NETWORKS, INC.'s involvement in industrial or automation systems.
  ["veth528"]="00:20:CF" # TEST & MEASUREMENT SYSTEMS INC # Relevant to OT due to TEST & MEASUREMENT SYSTEMS INC's involvement in industrial or automation systems.
  ["veth530"]="00:20:D1" # MICROCOMPUTER SYSTEMS (M) SDN. # Relevant to OT due to MICROCOMPUTER SYSTEMS (M) SDN.'s involvement in industrial or automation systems.
  ["veth533"]="00:20:D4" # Cabletron Systems, Inc. # Relevant to OT due to Cabletron Systems, Inc.'s involvement in industrial or automation systems.
  ["veth536"]="00:20:D7" # JAPAN MINICOMPUTER SYSTEMS CO., Ltd. # Relevant to OT due to JAPAN MINICOMPUTER SYSTEMS CO., Ltd.'s involvement in industrial or automation systems.
  ["veth543"]="00:20:DF" # KYOSAN ELECTRIC MFG. CO., LTD. # Relevant to OT due to KYOSAN ELECTRIC MFG. CO., LTD.'s involvement in industrial or automation systems.
  ["veth544"]="00:20:E0" # Actiontec Electronics, Inc # Relevant to OT due to Actiontec Electronics, Inc's involvement in industrial or automation systems.
  ["veth545"]="00:20:E1" # ALAMAR ELECTRONICS # Relevant to OT due to ALAMAR ELECTRONICS's involvement in industrial or automation systems.
  ["veth552"]="00:20:EA" # EFFICIENT NETWORKS, INC. # Relevant to OT due to EFFICIENT NETWORKS, INC.'s involvement in industrial or automation systems.
  ["veth554"]="00:20:EC" # TECHWARE SYSTEMS CORP. # Relevant to OT due to TECHWARE SYSTEMS CORP.'s involvement in industrial or automation systems.
  ["veth566"]="00:20:F9" # PARALINK NETWORKS, INC. # Relevant to OT due to PARALINK NETWORKS, INC.'s involvement in industrial or automation systems.
  ["veth567"]="00:20:FA" # GDE SYSTEMS, INC. # Relevant to OT due to GDE SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth575"]="00:40:0C" # GENERAL MICRO SYSTEMS, INC. # Relevant to OT due to GENERAL MICRO SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth577"]="00:40:10" # SONIC SYSTEMS, INC. # Relevant to OT due to SONIC SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth578"]="00:40:13" # NTT DATA COMM. SYSTEMS CORP. # Relevant to OT due to NTT DATA COMM. SYSTEMS CORP.'s involvement in industrial or automation systems.
  ["veth594"]="00:40:3F" # SSANGYONG COMPUTER SYSTEMS # Relevant to OT due to SSANGYONG COMPUTER SYSTEMS's involvement in industrial or automation systems.
  ["veth596"]="00:40:43" # Nokia Siemens Networks GmbH & Co. KG. # Relevant to OT due to Nokia Siemens Networks GmbH & Co. KG.'s involvement in industrial or automation systems.
  ["veth599"]="00:40:4D" # TELECOMMUNICATIONS TECHNIQUES # Relevant to OT due to TELECOMMUNICATIONS TECHNIQUES's involvement in industrial or automation systems.
  ["veth600"]="00:40:4F" # SPACE & NAVAL WARFARE SYSTEMS # Relevant to OT due to SPACE & NAVAL WARFARE SYSTEMS's involvement in industrial or automation systems.
  ["veth608"]="00:40:66" # APRESIA Systems Ltd # Relevant to OT due to APRESIA Systems Ltd's involvement in industrial or automation systems.
  ["veth610"]="00:40:68" # EXTENDED SYSTEMS # Relevant to OT due to EXTENDED SYSTEMS's involvement in industrial or automation systems.
  ["veth611"]="00:40:69" # LEMCOM SYSTEMS, INC. # Relevant to OT due to LEMCOM SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth612"]="00:40:6A" # KENTEK INFORMATION SYSTEMS,INC # Relevant to OT due to KENTEK INFORMATION SYSTEMS,INC's involvement in industrial or automation systems.
  ["veth617"]="00:40:78" # WEARNES AUTOMATION PTE LTD # Relevant to OT due to WEARNES AUTOMATION PTE LTD's involvement in industrial or automation systems.
  ["veth618"]="00:40:7F" # FLIR Systems # Relevant to OT due to FLIR Systems's involvement in industrial or automation systems.
  ["veth620"]="00:40:85" # SAAB INSTRUMENTS AB # Relevant to OT due to SAAB INSTRUMENTS AB's involvement in industrial or automation systems.
  ["veth623"]="00:40:8A" # TPS TELEPROCESSING SYS. GMBH # Relevant to OT due to TPS TELEPROCESSING SYS. GMBH's involvement in industrial or automation systems.
  ["veth631"]="00:40:96" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth633"]="00:40:9A" # NETWORK EXPRESS, INC. # Relevant to OT due to NETWORK EXPRESS, INC.'s involvement in industrial or automation systems.
  ["veth637"]="00:40:9F" # Telco Systems, Inc. # Relevant to OT due to Telco Systems, Inc.'s involvement in industrial or automation systems.
  ["veth638"]="00:40:A4" # ROSE ELECTRONICS # Relevant to OT due to ROSE ELECTRONICS's involvement in industrial or automation systems.
  ["veth640"]="00:40:AA" # Valmet Automation # Relevant to OT due to Valmet Automation's involvement in industrial or automation systems.
  ["veth642"]="00:40:AE" # DELTA CONTROLS, INC. # Relevant to OT due to DELTA CONTROLS, INC.'s involvement in industrial or automation systems.
  ["veth648"]="00:40:BD" # STARLIGHT NETWORKS, INC. # Relevant to OT due to STARLIGHT NETWORKS, INC.'s involvement in industrial or automation systems.
  ["veth649"]="00:40:C0" # VISTA CONTROLS CORPORATION # Relevant to OT due to VISTA CONTROLS CORPORATION's involvement in industrial or automation systems.
  ["veth660"]="00:40:D8" # OCEAN OFFICE AUTOMATION LTD. # Relevant to OT due to OCEAN OFFICE AUTOMATION LTD.'s involvement in industrial or automation systems.
  ["veth662"]="00:40:DF" # DIGALOG SYSTEMS, INC. # Relevant to OT due to DIGALOG SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth665"]="00:40:E3" # QUIN SYSTEMS LTD # Relevant to OT due to QUIN SYSTEMS LTD's involvement in industrial or automation systems.
  ["veth668"]="00:40:E7" # ARNOS INSTRUMENTS & COMPUTER # Relevant to OT due to ARNOS INSTRUMENTS & COMPUTER's involvement in industrial or automation systems.
  ["veth669"]="00:40:E9" # ACCORD SYSTEMS, INC. # Relevant to OT due to ACCORD SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth670"]="00:40:EA" # PLAIN TREE SYSTEMS INC # Relevant to OT due to PLAIN TREE SYSTEMS INC's involvement in industrial or automation systems.
  ["veth671"]="00:40:ED" # NETWORK CONTROLS INT'NATL INC. # Relevant to OT due to NETWORK CONTROLS INT'NATL INC.'s involvement in industrial or automation systems.
  ["veth673"]="00:40:F1" # CHUO ELECTRONICS CO., LTD. # Relevant to OT due to CHUO ELECTRONICS CO., LTD.'s involvement in industrial or automation systems.
  ["veth683"]="00:60:02" # SCREEN SUBTITLING SYSTEMS, LTD # Relevant to OT due to SCREEN SUBTITLING SYSTEMS, LTD's involvement in industrial or automation systems.
  ["veth690"]="00:60:09" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth697"]="00:60:10" # NETWORK MACHINES, INC. # Relevant to OT due to NETWORK MACHINES, INC.'s involvement in industrial or automation systems.
  ["veth699"]="00:60:12" # POWER COMPUTING CORPORATION # Relevant to OT due to POWER COMPUTING CORPORATION's involvement in industrial or automation systems.
  ["veth707"]="00:60:1A" # KEITHLEY INSTRUMENTS # Relevant to OT due to KEITHLEY INSTRUMENTS's involvement in industrial or automation systems.
  ["veth708"]="00:60:1B" # MESA ELECTRONICS # Relevant to OT due to MESA ELECTRONICS's involvement in industrial or automation systems.
  ["veth713"]="00:60:20" # PIVOTAL NETWORKING, INC. # Relevant to OT due to PIVOTAL NETWORKING, INC.'s involvement in industrial or automation systems.
  ["veth715"]="00:60:22" # VICOM SYSTEMS, INC. # Relevant to OT due to VICOM SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth718"]="00:60:25" # ACTIVE IMAGING PLC # Relevant to OT due to ACTIVE IMAGING PLC's involvement in industrial or automation systems.
  ["veth719"]="00:60:26" # VIKING Modular Solutions # Relevant to OT due to VIKING Modular Solutions's involvement in industrial or automation systems.
  ["veth728"]="00:60:2F" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth730"]="00:60:31" # HRK SYSTEMS # Relevant to OT due to HRK SYSTEMS's involvement in industrial or automation systems.
  ["veth737"]="00:60:38" # Nortel Networks # Relevant to OT due to Nortel Networks's involvement in industrial or automation systems.
  ["veth739"]="00:60:3A" # QUICK CONTROLS LTD. # Relevant to OT due to QUICK CONTROLS LTD.'s involvement in industrial or automation systems.
  ["veth743"]="00:60:3E" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth752"]="00:60:47" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth758"]="00:60:4D" # MMC NETWORKS, INC. # Relevant to OT due to MMC NETWORKS, INC.'s involvement in industrial or automation systems.
  ["veth765"]="00:60:54" # CONTROLWARE GMBH # Relevant to OT due to CONTROLWARE GMBH's involvement in industrial or automation systems.
  ["veth767"]="00:60:56" # NETWORK TOOLS, INC. # Relevant to OT due to NETWORK TOOLS, INC.'s involvement in industrial or automation systems.
  ["veth772"]="00:60:5C" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth778"]="00:60:63" # PSION DACOM PLC. # Relevant to OT due to PSION DACOM PLC.'s involvement in industrial or automation systems.
  ["veth780"]="00:60:65" # B&R Industrial Automation GmbH # Relevant to OT due to B&R Industrial Automation GmbH's involvement in industrial or automation systems.
  ["veth784"]="00:60:69" # Brocade Communications Systems LLC # Relevant to OT due to Brocade Communications Systems LLC's involvement in industrial or automation systems.
  ["veth791"]="00:60:70" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth796"]="00:60:77" # PRISA NETWORKS # Relevant to OT due to PRISA NETWORKS's involvement in industrial or automation systems.
  ["veth797"]="00:60:78" # POWER MEASUREMENT LTD. # Relevant to OT due to POWER MEASUREMENT LTD.'s involvement in industrial or automation systems.
  ["veth800"]="00:60:7B" # FORE SYSTEMS, INC. # Relevant to OT due to FORE SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth802"]="00:60:7D" # SENTIENT NETWORKS INC. # Relevant to OT due to SENTIENT NETWORKS INC.'s involvement in industrial or automation systems.
  ["veth808"]="00:60:83" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
  ["veth810"]="00:60:87" # KANSAI ELECTRIC CO., LTD. # Relevant to OT due to KANSAI ELECTRIC CO., LTD.'s involvement in industrial or automation systems.
  ["veth817"]="00:60:8E" # HE ELECTRONICS, TECHNOLOGIE & SYSTEMTECHNIK GmbH # Relevant to OT due to HE ELECTRONICS, TECHNOLOGIE & SYSTEMTECHNIK GmbH's involvement in industrial or automation systems.
  ["veth819"]="00:60:90" # Artiza Networks Inc # Relevant to OT due to Artiza Networks Inc's involvement in industrial or automation systems.
  ["veth820"]="00:60:91" # FIRST PACIFIC NETWORKS, INC. # Relevant to OT due to FIRST PACIFIC NETWORKS, INC.'s involvement in industrial or automation systems.
  ["veth824"]="00:60:95" # ACCU-TIME SYSTEMS, INC. # Relevant to OT due to ACCU-TIME SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth835"]="00:60:A0" # SWITCHED NETWORK TECHNOLOGIES, INC. # Relevant to OT due to SWITCHED NETWORK TECHNOLOGIES, INC.'s involvement in industrial or automation systems.
  ["veth840"]="00:60:A5" # PERFORMANCE TELECOM CORP. # Relevant to OT due to PERFORMANCE TELECOM CORP.'s involvement in industrial or automation systems.
  ["veth841"]="00:60:A6" # PARTICLE MEASURING SYSTEMS # Relevant to OT due to PARTICLE MEASURING SYSTEMS's involvement in industrial or automation systems.
  ["veth849"]="00:60:AE" # TRIO INFORMATION SYSTEMS AB # Relevant to OT due to TRIO INFORMATION SYSTEMS AB's involvement in industrial or automation systems.
  ["veth853"]="00:60:B2" # PROCESS CONTROL CORP. # Relevant to OT due to PROCESS CONTROL CORP.'s involvement in industrial or automation systems.
  ["veth861"]="00:60:BA" # SAHARA NETWORKS, INC. # Relevant to OT due to SAHARA NETWORKS, INC.'s involvement in industrial or automation systems.
  ["veth862"]="00:60:BB" # Cabletron Systems, Inc. # Relevant to OT due to Cabletron Systems, Inc.'s involvement in industrial or automation systems.
  ["veth863"]="00:60:BC" # KeunYoung Electronics & Communication Co., Ltd. # Relevant to OT due to KeunYoung Electronics & Communication Co., Ltd.'s involvement in industrial or automation systems.
  ["veth866"]="00:60:BF" # MACRAIGOR SYSTEMS, INC. # Relevant to OT due to MACRAIGOR SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth867"]="00:60:C0" # Nera Networks AS # Relevant to OT due to Nera Networks AS's involvement in industrial or automation systems.
  ["veth871"]="00:60:C4" # SOLITON SYSTEMS K.K. # Relevant to OT due to SOLITON SYSTEMS K.K.'s involvement in industrial or automation systems.
  ["veth875"]="00:60:C8" # KUKA WELDING SYSTEMS & ROBOTS # Relevant to OT due to KUKA WELDING SYSTEMS & ROBOTS's involvement in industrial or automation systems.
  ["veth876"]="00:60:C9" # ControlNet, Inc. # Relevant to OT due to ControlNet, Inc.'s involvement in industrial or automation systems.
  ["veth877"]="00:60:CA" # HARMONIC SYSTEMS INCORPORATED # Relevant to OT due to HARMONIC SYSTEMS INCORPORATED's involvement in industrial or automation systems.
  ["veth881"]="00:60:CF" # ALTEON NETWORKS, INC. # Relevant to OT due to ALTEON NETWORKS, INC.'s involvement in industrial or automation systems.
  ["veth884"]="00:60:D2" # LUCENT TECHNOLOGIES TAIWAN TELECOMMUNICATIONS CO., LTD. # Relevant to OT due to LUCENT TECHNOLOGIES TAIWAN TELECOMMUNICATIONS CO., LTD.'s involvement in industrial or automation systems.
  ["veth890"]="00:60:D8" # ELMIC SYSTEMS, INC. # Relevant to OT due to ELMIC SYSTEMS, INC.'s involvement in industrial or automation systems.
  ["veth891"]="00:60:DA" # Red Lion Controls, LP # Relevant to OT due to Red Lion Controls, LP's involvement in industrial or automation systems.
  ["veth896"]="00:60:DF" # Brocade Communications Systems LLC # Relevant to OT due to Brocade Communications Systems LLC's involvement in industrial or automation systems.
  ["veth900"]="00:60:E3" # ARBIN INSTRUMENTS # Relevant to OT due to ARBIN INSTRUMENTS's involvement in industrial or automation systems.
  ["veth902"]="00:60:E5" # FUJI AUTOMATION CO., LTD. # Relevant to OT due to FUJI AUTOMATION CO., LTD.'s involvement in industrial or automation systems.
  ["veth903"]="00:60:E6" # SHOMITI SYSTEMS INCORPORATED # Relevant to OT due to SHOMITI SYSTEMS INCORPORATED's involvement in industrial or automation systems.
  ["veth908"]="00:60:EB" # FOURTHTRACK SYSTEMS # Relevant to OT due to FOURTHTRACK SYSTEMS's involvement in industrial or automation systems.
  ["veth909"]="00:60:EC" # HERMARY OPTO ELECTRONICS INC. # Relevant to OT due to HERMARY OPTO ELECTRONICS INC.'s involvement in industrial or automation systems.
  ["veth910"]="00:60:ED" # RICARDO TEST AUTOMATION LTD. # Relevant to OT due to RICARDO TEST AUTOMATION LTD.'s involvement in industrial or automation systems.
  ["veth915"]="00:60:F3" # Performance Analysis Broadband, Spirent plc # Relevant to OT due to Performance Analysis Broadband, Spirent plc's involvement in industrial or automation systems.
  ["veth916"]="00:60:F4" # ADVANCED COMPUTER SOLUTIONS, Inc. # Relevant to OT due to ADVANCED COMPUTER SOLUTIONS, Inc.'s involvement in industrial or automation systems.
  ["veth918"]="00:60:F7" # DATAFUSION SYSTEMS # Relevant to OT due to DATAFUSION SYSTEMS's involvement in industrial or automation systems.
)

case "$1" in
  create)
    if ! ip link show br0 &> /dev/null; then
        echo "Creating bridge br0..."
        sudo ip link add name br0 type bridge
        sudo ip addr add 10.10.10.1/24 dev br0
        sudo ip link set br0 up
    else
        echo "Bridge br0 already exists."
    fi

    counter=2
    for iface in "${!vendors[@]}"; do
        mac_prefix=${vendors[$iface]}
        mac="${mac_prefix}:$(printf "%02x" $((RANDOM%256))):$(printf "%02x" $((RANDOM%256))):$(printf "%02x" $((RANDOM%256)))"

        echo "iface: $iface , mac: $mac "
        sudo ip link add link br0 name "$iface" type macvlan mode bridge
        sudo ip link set "$iface" address "$mac"
        sudo ip addr add "10.10.10.$((counter + 1))/24" dev "$iface"
        sudo ip link set "$iface" up

        echo "$iface created with MAC $mac and IP 10.10.10.$((counter + 1))"
        ((counter++))
    done
    ;;
  destroy)
    for iface in "${!vendors[@]}"; do
        if ip link show "$iface" &> /dev/null; then
            echo "Deleting interface $iface..."
            sudo ip link delete "$iface"
        else
            echo "Interface $iface does not exist."
        fi
    done

    if ip link show br0 &> /dev/null; then
        echo "Deleting bridge br0..."
        sudo ip link set br0 down
        sudo ip link delete br0 type bridge
    else
        echo "Bridge br0 does not exist."
    fi
    ;;
  ping)
    while :
    do
      for iface in "${!vendors[@]}"; do
        ping -c1 -I $iface 10.10.10.254
        sleep 0.25
      done
      sleep 10
    done
    ;;
  *)
    echo "Usage: $0 {create|destroy|ping}"
    exit 1
    ;;
esac
