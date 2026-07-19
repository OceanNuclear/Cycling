import numpy as np

groupsets = {
"GRX groupset":
    (
        np.array([11,12,14,16,18,20,22,25,28,32]),
        [46, 30]
    ),

"CUBE Nulane ONE: Shimano Essa":
    (
        np.array([11,13,15,18,22,27,35,45]),
        [40]
    ),

"HYB 8.9: Shimano’s Deore 12 speed":
    (
        np.array([10,12,14,16,18,21,24,28,33,39,45,51]),
        [44]
    ),

"HYB 8.8: Shimano Deore's 10 speed":
    (
        np.array([11,13,15,18,21,24,28,34,40,46]),
        [44]
    ),

"CUBE Nuroad PRO: RX610":
    (
        np.array([10,12,14,16,18,21,24,28,33,39,45,51]), # Shimano Deore CS-M6100, 10-51T
        [40], # Shimano GRX FC-RX610, 40T
    ),

}

NUM_CHAR = 3+2

if __name__=='__main__':
    for name, (cassette, crank_set) in groupsets.items():
        print(f"For group set {name}, the gearing ratios are: {len(crank_set)}x{len(cassette)} gears:")
        all_ratios = []
        for crank_num, crank_ring in enumerate(crank_set):
            for cass_num, ratio in enumerate(crank_ring/cassette):
                is_cross_chaining = (cass_num==(len(cassette)-1)) and (crank_num==0)
                is_cross_chaining |= (cass_num==0) and (crank_num==(len(crank_set)-1))
                all_ratios.append(("{:.2f}".format(ratio), crank_num, is_cross_chaining))
        all_ratios = sorted(all_ratios)

        for crank_num in range(len(crank_set)):
            this_line = ""
            for ratio_str, _crank_num, is_cross_chaining in all_ratios:
                if _crank_num==crank_num:
                    # check for cross-chaining
                    if is_cross_chaining and len(crank_set)>1:
                        this_line += f"({ratio_str})"
                    else:
                        this_line += f" {ratio_str} "
                else:
                    this_line += " " * 6
            print(this_line)
        print()