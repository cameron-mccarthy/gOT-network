
#!/bin/bash

declare -A vendors=(
["veth0"]="00:00:0C" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
["veth1"]="00:00:0C" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
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
["veth101"]="00:10:14" # Cisco Systems, Inc # Relevant to OT due to Cisco Systems, Inc's involvement in industrial or automation systems.
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
["veth295"]="00:10:DB" # Juniper Networks # Relevant to OT due to Juniper Networks's involvement in industrial or automation systems.
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
)

PHYS_IF="enxa0cec8a60835"
IP_BASE="172.25.4"
START_IP=151
END_IP=254
SKIP_IP=42

case "$1" in
  create)
    if ! ip link show "$PHYS_IF" &> /dev/null; then
        echo "Physical interface $PHYS_IF not found. Exiting."
        exit 1
    fi

    ip_counter=$START_IP
    for iface in "${!vendors[@]}"; do
        # Skip disallowed IPs
        while [[ "$ip_counter" -eq "$SKIP_IP" ]]; do
            ((ip_counter++))
        done

        if [[ "$ip_counter" -gt "$END_IP" ]]; then
            echo "No more valid IPs available in range $IP_BASE.$START_IP to $IP_BASE.$END_IP"
            exit 1
        fi

        mac_prefix=${vendors[$iface]}
        mac="${mac_prefix}:$(printf "%02x" $((RANDOM%256))):$(printf "%02x" $((RANDOM%256))):$(printf "%02x" $((RANDOM%256)))"
        ip_addr="${IP_BASE}.${ip_counter}"

        echo "Creating $iface with MAC $mac and IP $ip_addr on $PHYS_IF..."
        sudo ip link add link "$PHYS_IF" name "$iface" type macvlan mode bridge
        sudo ip link set "$iface" address "$mac"
        sudo ip addr add "$ip_addr/24" dev "$iface"
        sudo ip link set "$iface" up

        ((ip_counter++))
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
    ;;
  ping)
    while :
    do
      for iface in "${!vendors[@]}"; do
        ping -c1 -I "$iface" 172.25.4.1
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
