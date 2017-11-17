#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kbates
#
# Created:     22/09/2016
# Copyright:   (c) kbates 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import Tkinter
root = Tkinter.Tk()

# ACARS takeoff data page 1/5
#
#
def Page1():
        nw = Tkinter.Tk()
        nw.wm_geometry("500x300")

        #previous and next page buttons
        perf_up1_b1 = Tkinter.Button(nw, text="< Prev", borderwidth=1).grid(row=0, column=0, padx=0)
        perf_up1_b2 = Tkinter.Button(nw, text="Next >", borderwidth=1, command= Page2).grid(row=0, column=4, padx=0)
        #acars_pg_b3 = Tkinter.Button(nw, text="Page 3", borderwidth=1).grid(row=0, column=3, padx=0)
        #acars_pg_b4 = Tkinter.Button(nw, text="Page 4", borderwidth=1).grid(row=0, column=4, padx=0)
        #acars_pg_b5 = Tkinter.Button(nw, text="Page 5", borderwidth=1).grid(row=0, column=5, padx=0)

        #title for page 1
        page1_title_label = Tkinter.Label(nw, text="ACARS TAKEOFF DATA 1/5").grid(row=1, column=2,pady=10)

        #first row of page 1 perf uplink upgrade #1
        perf_up1_fltno = Tkinter.Label(nw, text="FLT NO").grid(row=2, column=1)
        perf_up1_fltno_ent = Tkinter.Entry(nw, bd=1, justify="center").grid(row=3,column=1)

        perf_up1_rls = Tkinter.Label(nw, text="RLS/WB").grid(row=2, column=2)
        perf_up1_rls_ent = Tkinter.Entry(nw, bd=1, justify="center").grid(row=3, column=2)

        acars_pg_time = Tkinter.Label(nw, text="TIME").grid(row=2, column=3)
        perf_up1_time_ent = Tkinter.Entry(nw, bd=1, justify="center").grid(row=3, column=3)

        #second row of page 1 perf uplink upgrade #1
        perf_up1_wind = Tkinter.Label(nw, text="WIND").grid(row=4, column=1)
        perf_up1_wind_ent = Tkinter.Entry(nw, bd=1, justify="center").grid(row=5,column=1)

        perf_up1_oat = Tkinter.Label(nw, text="OAT*C").grid(row=4, column=2)
        perf_up1_oat_ent = Tkinter.Entry(nw, bd=1, justify="center").grid(row=5,column=2)

        perf_up1_qnh = Tkinter.Label(nw, text="QNH").grid(row=4, column=3)
        perf_up1_qnh_ent = Tkinter.Entry(nw, bd=1, justify="center").grid(row=5,column=3)

        #third row
        perf_up1_pax = Tkinter.Label(nw, text="PAX").grid(row=6, column=1)
        perf_up1_pax_ent = Tkinter.Entry(nw, bd=1, justify="center").grid(row=7,column=1)

        perf_up1_cargo = Tkinter.Label(nw, text="CARGO").grid(row=6, column=2)
        perf_up1_cargo_ent = Tkinter.Entry(nw, bd=1, justify="center").grid(row=7,column=2)

        perf_up1_zfw = Tkinter.Label(nw, text="ZFW  /  CG").grid(row=6, column=3)
        perf_up1_zfw_ent = Tkinter.Entry(nw, bd=1, justify="center").grid(row=7,column=3)
        perf_up1_zfw_cg = Tkinter.Label(nw, text="XX.X").grid(row=7, column=4)

        #4th row
        perf_up1_agent = Tkinter.Label(nw, text="AGENT").grid(row=8, column=1)
        perf_up1_agent_ent = Tkinter.Entry(nw, bd=1, justify="center").grid(row=9,column=1)

        perf_up1_fob = Tkinter.Label(nw, text="FOB").grid(row=8, column=3)
        perf_up1_fob_ent = Tkinter.Entry(nw, bd=1, justify="center").grid(row=9, column=3)

        #5th Row
        perf_up1_phone = Tkinter.Label(nw, text="PHONE").grid(row=10, column=1)
        perf_up1_phone_ent = Tkinter.Entry(nw, bd=1, justify="center").grid(row=11, column=1)

        perf_up1_gtow = Tkinter.Label(nw, text="GTOW  /  CG").grid(row=10, column=3)
        perf_up1_gtow_ent = Tkinter.Entry(nw, bd=1, justify="center").grid(row=11,column=3)
        perf_up1_gtow_cg = Tkinter.Label(nw, text="XX.X").grid(row=11, column=4)

# ACARS takeoff data page 2/5
#
#
def Page2():
        nw = Tkinter.Tk()
        nw.wm_geometry("500x300")

        page2_prev_button = Tkinter.Button(nw, text="< Prev", borderwidth=1, command= Page1).grid(row=0, column=0, padx=0)
        page2_next_button = Tkinter.Button(nw, text="Next >", borderwidth=1, command= Page3).grid(row=0, column=3, pady=0)

        page2__title_label = Tkinter.Label(nw, text="ACARS TAKEOFF DATA 2/5").grid(row=1, column=1,pady=10)

        page2_remarks_label = Tkinter.Label(nw, text="REMARKS").grid(row=2, column=0)
        page2_label_1 = Tkinter.Label(nw, text="1").grid(row=3, column=0)
        page2_entry_1 = Tkinter.Entry(nw, bd=1, width=65).grid(row=3, column=1)

        page2_label_2 = Tkinter.Label(nw, text="2").grid(row=4, column=0)
        page2_entry_2 = Tkinter.Entry(nw, bd=1, width=65).grid(row=4, column=1)

        page2_label_3 = Tkinter.Label(nw, text="3").grid(row=5, column=0)
        page2_entry_3 = Tkinter.Entry(nw, bd=1, width=65).grid(row=5, column=1)

        page2_label_4 = Tkinter.Label(nw, text="4").grid(row=6, column=0)
        page2_entry_4 = Tkinter.Entry(nw, bd=1, width=65).grid(row=6, column=1)

        page2_label_5 = Tkinter.Label(nw, text="5").grid(row=7, column=0)
        page2_entry_5 = Tkinter.Entry(nw, bd=1, width=65).grid(row=7, column=1)

        page2_label_6 = Tkinter.Label(nw, text="6").grid(row=8, column=0)
        page2_entry_6 = Tkinter.Entry(nw, bd=1, width=65).grid(row=8, column=1)

        page2_label_7 = Tkinter.Label(nw, text="7").grid(row=9, column=0)
        page2_entry_7 = Tkinter.Entry(nw, bd=1, width=65).grid(row=9, column=1)

        page2_label_8 = Tkinter.Label(nw, text="8").grid(row=10, column=0)
        page2_entry_8 = Tkinter.Entry(nw, bd=1, width=65).grid(row=10, column=1)

        page2_label_9 = Tkinter.Label(nw, text="9").grid(row=11, column=0)
        page2_entry_9 = Tkinter.Entry(nw, bd=1, width=65).grid(row=11, column=1)

# ACARS takeoff data page 3/5
#
#
def Page3():
        nw = Tkinter.Tk()
        nw.wm_geometry("500x300")

        page3_prev_button = Tkinter.Button(nw, text="< Prev", borderwidth=1).grid(row=0, column=0, padx=0)
        page3_next_button = Tkinter.Button(nw, text="Next >", borderwidth=1, command= Page4).grid(row=0, column=4, pady=0)
        page3_title_label = Tkinter.Label(nw, text="ACARS TAKEOFF DATA 3/5").grid(row=1, column=2,pady=10)

        page3_length_label = Tkinter.Label(nw, text="LENGTH").grid(row=3, column=1)
        page3_length_entry = Tkinter.Entry(nw, bd=1, justify="center", width=12).grid(row=4, column=1)

        page3_airp_entry = Tkinter.Entry(nw, bd=1, justify="center", width=12).grid(row=3, column=2)
        page3_rwy_entry = Tkinter.Entry(nw, bd=1, justify="center", width=12).grid(row=4, column=2)

        page3_dth_entry = Tkinter.Entry(nw, bd=1, justify="center", width=40).grid(row=5, column=2, pady=3)
        page3_dto1_entry = Tkinter.Entry(nw, bd=1, justify="center", width=40).grid(row=6, column=2)

        page3_shift_label = Tkinter.Label(nw, text="SHIFT").grid(row=3, column=3)
        page3_shift_entry = Tkinter.Entry(nw, bd=1, justify="center", width=12).grid(row=4, column=3)

        page3_flaps_label = Tkinter.Label(nw, text="FLAPS").grid(row=7, column=1)
        page3_flaps_entry = Tkinter.Entry(nw, bd=1, justify="center", width=12).grid(row=8, column=1)

        page3_sel_label = Tkinter.Label(nw, text="SEL").grid(row=9, column=1)
        page3_sel_entry = Tkinter.Entry(nw, bd=1, justify="center", width=12).grid(row=10, column=1)

        page3_eofra_label = Tkinter.Label(nw, text="E/O FRA").grid(row=11, column=1)
        page3_eofra_entry = Tkinter.Entry(nw, bd=1, justify="center", width=12).grid(row=12, column=1)

        page3_mrtw_label = Tkinter.Label(nw, text="MRTW").grid(row=7, column=2)
        page3_mrtw_entry = Tkinter.Entry(nw, bd=1, justify="center", width=12).grid(row=8, column=2)

        page3_mtow_label = Tkinter.Label(nw, text="MTOW").grid(row=9, column=2)
        page3_mtow_entry = Tkinter.Entry(nw, bd=1, justify="center", width=12).grid(row=10, column=2)


        page3_gtow_cg_label = Tkinter.Label(nw, text="GTOW/CG").grid(row=11, column=2)
        page3_gtow_cg_label2 = Tkinter.Entry(nw, bd=1, state="disable", width=12).grid(row=12, column=2)

        page3_v1_label = Tkinter.Label(nw, text="V1").grid(row=7, column=3)
        page3_v1_entry = Tkinter.Entry(nw, bd=1, justify="center", width=12).grid(row=8, column=3)

        page3_vr_label = Tkinter.Label(nw, text="VR").grid(row=9, column=3)
        page3_vr_entry = Tkinter.Entry(nw, bd=1, justify="center", width=12).grid(row=10, column=3)

        page3_v2_label = Tkinter.Label(nw, text="V2").grid(row=11, column=3)
        page3_v2_entry = Tkinter.Entry(nw, bd=1, justify="center", width=12).grid(row=12, column=3)

#Perf Init Page 1
#
#
#
def Page4():
        nw = Tkinter.Tk()
        nw.wm_geometry("500x300")

        page4_prev_button = Tkinter.Button(nw, text="< Prev", borderwidth=1).grid(row=0, column=0, padx=0)
        page4_next_button = Tkinter.Button(nw, text="Next >", borderwidth=1).grid(row=0, column=4, pady=0, sticky="w")
        page4_title_label = Tkinter.Label(nw, text="PERF INIT 1/2").grid(row=1, column=2,pady=10)

        page4_gw_crz_cg_label = Tkinter.Label(nw, text="GW/CRZ CG").grid(row=2, column=1)
        page4_gw_crz_cg_label2 = Tkinter.Entry(nw, bd=1, state="disable").grid(row=3, column=1)

        page4_plan_label = Tkinter.Label(nw, text="PLAN/FUEL").grid(row=4, column=1)
        page4_plan_entry = Tkinter.Entry(nw, bd=1, state="disable").grid(row=5, column=1)

        pag4_zfw_label = Tkinter.Label(nw, text="ZFW").grid(row=6, column=1)
        pag4_zfw_entry = Tkinter.Entry(nw, bd=1, justify="center").grid(row=7, column=1)

        page4_reserve_label = Tkinter.Label(nw, text="RESERVE").grid(row=8, column=1)
        page4_reserve_entry = Tkinter.Entry(nw, bd=1, state="disable").grid(row=9, column=1)

        page4_cost_index_label = Tkinter.Label(nw, text="COST INDEX").grid(row=10, column=1)
        page4_cost_index_entry = Tkinter.Entry(nw, bd=1, state="disable").grid(row=11, column=1)

        page4_cost_index_label = Tkinter.Label(nw, text="COST INDEX").grid(row=10, column=1, padx=40)
        page4_cost_index_entry = Tkinter.Entry(nw, bd=1, state="disable").grid(row=11, column=1)

        page4_crz_alt_label = Tkinter.Label(nw, text="CRZ ALT").grid(row=2, column=3, padx=40)
        page4_crz_alt_entry = Tkinter.Entry(nw, bd=1, state="disable").grid(row=3, column=3)

        page4_crz_wind_label = Tkinter.Label(nw, text="CRZ WIND").grid(row=4, column=3)
        page4_crz_wind_entry = Tkinter.Entry(nw, bd=1, state="disable").grid(row=5, column=3)

        page4_tc_oat_label = Tkinter.Label(nw, text="T/C OAT").grid(row=6, column=3)
        page4_tc_oat_entry = Tkinter.Entry(nw, bd=1, state="disable").grid(row=7, column=3)

        page4_trans_alt_label= Tkinter.Label(nw, text="TRANS ALT").grid(row=8, column=3)
        page4_crz_alt_label2 = Tkinter.Label(nw, text="18000").grid(row=9, column=3)

# Takeoff Ref Uplink Page 1/2
#
#
def Page5():
        nw = Tkinter.Tk()
        nw.wm_geometry("500x300")





main_l1 = Tkinter.Label(text="ACARS SCENARIO GENERATOR", borderwidth=1).grid(row=0, column=0, padx=15, pady=5)
main_b1 = Tkinter.Button(root, text="PERF UPLINK UPG #1", borderwidth=1, command= Page1).grid(row=1, column=0)
main_b2 = Tkinter.Button(root, text="PERF UPLINK UPG #2", borderwidth=1, command= Page1).grid(row=2, column=0)
main_b3 = Tkinter.Button(root, text="PERF UPLINK UPG #3", borderwidth=1, command= Page1).grid(row=3, column=0)
main_b4 = Tkinter.Button(root, text="REC SESSION #11", borderwidth=1, padx=11, command= Page1).grid(row=4, column=0)
main_b5 = Tkinter.Button(root, text="REC SESSION #12", borderwidth=1, padx=11, command= Page1).grid(row=5, column=0)
main_b6 = Tkinter.Button(root, text="LOFT", borderwidth=1, padx=43, command= Page1).grid(row=6, column=0)
main_b7 = Tkinter.Button(root, text="CHECK RIDES", borderwidth=1, padx=21, command= Page1).grid(row=7, column=0)

#l1.pack()
#b1.pack()


#for r in range(3):
#    Tkinter.Button(root, text="Page 1")
#    for c in range(4):
#        Tkinter.Label(root, text='test',
#           borderwidth=1 ).grid(row=r,column=c)

root.wm_geometry("200x210")
root.mainloop()
