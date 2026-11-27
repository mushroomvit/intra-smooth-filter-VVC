# Voltus_rail Command File

#Result directory
setvar output_directory_name /home/weber/PESSOAL/intra-smooth-filter-VVC/backend/lay/reports/20261125_115837-65-SGPF-u65-ring02/postcts_era/results

#Distributed processing setting
setvar max_cpu 1
setvar nga_enabled true
nga_dp_hosts max_cpu=1 mode=local time_out=3600

#Layout Files
layout_file /home/weber/PESSOAL/intra-smooth-filter-VVC/backend/lay/work/20261125_115837-65-SGPF-u65-ring02/innovus_temp_3470101_e4d4ab6c-7b64-4fb0-93f3-fbff8d4f86b5_server_ci_inovador_weber_NceDwY/eps_out_3470101.def.gz

#Cell Library
cell_library /home/weber/PESSOAL/intra-smooth-filter-VVC/backend/lay/reports/20261125_115837-65-SGPF-u65-ring02/postcts_era/results/era_work/incremental_output0/pgv/techonly.cl 
setvar tesla_accuracy_mode xd
use_cell_view type standard fast
use_cell_view type macro fast
use_cell_view type io fast
use_cell_view type powergate fast
setvar unified_power_switch_flow true
setvar power_up_fast_mode true
setvar work_directory_name /home/weber/PESSOAL/intra-smooth-filter-VVC/backend/lay/reports/20261125_115837-65-SGPF-u65-ring02/postcts_era/work
setvar report_msmv_format true
setvar compress_powergrid_database false
setvar hierarchy_char /
setvar generate_multi_voltage_library true
setvar use_cell_id true
nga_setvar nga_enable_new_transient_analysis true
setvar enable_smx true
setvar ignore_shorts true
setvar enable_manufacturing_effects false
setvar cluster_via1_ports true
setvar ignore_fillers true
setvar ignore_decaps true
setvar em_redundancy_via_current_threshold 0.0
setvar temperature 25
setvar gif_zoom_topcell_diearea false
setvar tech_file /home/tools/design_kits/tsmc/22/digital/CapTbl_qrcdeck_5X1Z/RC_QRC_cln22ulp_1p7m_5x1z_tfr6_ut-alrdl_9corners_shrink_1.1p1a/RC_QRC_cln22ulp_1p07m+ut-alrdl_5x1z_typical/qrcTechFile
setvar em_deltaT 5
setvar keep_log false
setvar enable_report_db true
setvar eiv_report_auto true
nga_setvar nga_current_redistribution true
setvar mge_load_static_pti false
nga_setvar nga_protect_rail_simulation_time false
setvar halt_on_net_with_no_cell_connections false
setvar enable_scheduler true

#Layout Files
layout_file /home/weber/PESSOAL/intra-smooth-filter-VVC/backend/lay/reports/20261125_115837-65-SGPF-u65-ring02/postcts_era/results/era_work/incremental_output0/defs/VDD.def.gz

#Layout Files
layout_file /home/weber/PESSOAL/intra-smooth-filter-VVC/backend/lay/reports/20261125_115837-65-SGPF-u65-ring02/postcts_era/results/era_work/incremental_output0/defs/VSS.def.gz
layout_file -lef /home/tools/design_kits/tsmc/22/digital/CapTbl_qrcdeck_5X1Z/PRTF_Innovus_22nm_001_Cad_V16b/PRTF_Innovus_22nm_001_Cad_V16b/PR_tech/Cadence/LefHeader/VHV/PRTF_Innovus_N22_7M_5X1Z_RDL_7T.16b.tlef
layout_file -lef /home/tools/design_kits/tsmc/22/digital/TSMCHOME/digital/Back_End/lef/tcbn22ullbwp7t40p140sg_110a/lef/tcbn22ullbwp7t40p140sg.lef
layout_file -lef /home/tools/design_kits/tsmc/22/digital/TSMCHOME/digital/Back_End/lef/tcbn22ullbwp7t40p140sguhvt_110a/lef/tcbn22ullbwp7t40p140sguhvt.lef
layout_file -lef /home/tools/design_kits/tsmc/22/digital/TSMCHOME/digital/Back_End/lef/tcbn22ullbwp7t40p140mbsg_110a/lef/tcbn22ullbwp7t40p140mbsg.lef
layout_file -lef /home/tools/design_kits/tsmc/22/digital/TSMCHOME/digital/Back_End/lef/tcbn22ullbwp7t40p140mbsguhvt_110a/lef/tcbn22ullbwp7t40p140mbsguhvt.lef
layout_file -lef /home/tools/design_kits/tsmc/22/digital/TSMCHOME/digital/Back_End/lef/tcbn22ullbwp7t40p140pmsg_110a/lef/tcbn22ullbwp7t40p140pmsg.lef
layout_file -lef /home/tools/design_kits/tsmc/22/digital/TSMCHOME/digital/Back_End/lef/tcbn22ullbwp7t40p140pmsguhvt_110a/lef/tcbn22ullbwp7t40p140pmsguhvt.lef
net_voltage VDD 0.8 0.72
power_pin_supply_tolerance 0.56 1.04 net=VDD
net_voltage VSS 0 0.08
power_pin_supply_tolerance 0 0.3 net=VSS
power_domain CORE pwrnet="VDD" gndnet="VSS"
current_data_file /home/weber/PESSOAL/intra-smooth-filter-VVC/backend/lay/reports/20261125_115837-65-SGPF-u65-ring02/power/cts/static_VDD.ptiavg
current_data_file /home/weber/PESSOAL/intra-smooth-filter-VVC/backend/lay/reports/20261125_115837-65-SGPF-u65-ring02/power/cts/static_VSS.ptiavg
power_pin VDD file=/home/weber/PESSOAL/intra-smooth-filter-VVC/backend/lay/reports/20261125_115837-65-SGPF-u65-ring02/era/VDD.pp
power_pin VDD file=/home/weber/PESSOAL/intra-smooth-filter-VVC/backend/lay/reports/20261125_115837-65-SGPF-u65-ring02/postcts_era/VDD.pp
power_pin VSS file=/home/weber/PESSOAL/intra-smooth-filter-VVC/backend/lay/reports/20261125_115837-65-SGPF-u65-ring02/era/VSS.pp
power_pin VSS file=/home/weber/PESSOAL/intra-smooth-filter-VVC/backend/lay/reports/20261125_115837-65-SGPF-u65-ring02/postcts_era/VSS.pp
power_pin VDD file=/home/weber/PESSOAL/intra-smooth-filter-VVC/backend/lay/reports/20261125_115837-65-SGPF-u65-ring02/era/VDD.pp
power_pin VDD file=/home/weber/PESSOAL/intra-smooth-filter-VVC/backend/lay/reports/20261125_115837-65-SGPF-u65-ring02/postcts_era/VDD.pp
power_pin VSS file=/home/weber/PESSOAL/intra-smooth-filter-VVC/backend/lay/reports/20261125_115837-65-SGPF-u65-ring02/era/VSS.pp
power_pin VSS file=/home/weber/PESSOAL/intra-smooth-filter-VVC/backend/lay/reports/20261125_115837-65-SGPF-u65-ring02/postcts_era/VSS.pp
analyze CORE 0.8 avg 0.10 ir tc rc iv rv vc pv pi
