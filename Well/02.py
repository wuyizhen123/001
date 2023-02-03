import wellbore_trajectories as wp
import pandas as pd
from copy import deepcopy
# well = wp.load('trajectory2.xlsx')   # 加载数据
# print(well.get_point(741, depth_type='md'))     # 得到3750m井深处的的数据

# well = wp.get(3000,   # 目标井深 (md) 单位 m
#               profile='V',    # 设置剖面类型
#               set_info={'dlsResolution': 30, 'wellType': 'offshore', 'units': 'metric'},
#
#               points=100,   # (可选参数）定义轨迹点的个数
#               set_start={'north': 0, 'east': 0, 'depth': 0})    # (可选参数) 设置初始点

well = wp.load('HW1113.xlsx', inner_points=5)   # loading file with only original survey points
well.plot(style={'color': 'dls'}).show()

# well = wp.load('trajectory2.xlsx')
# qwe = pd.DataFrame(well.trajectory)
# print(well.trajectory)
# print((qwe))
# well.interp_any_point(40,depth_type='tvd')
# qwe = pd.DataFrame(well.trajectory)
# print(well.trajectory)
# print((qwe))
# well = wp.load('trajectory2.xlsx')
# well1 = deepcopy(well)
# print(id(well))
# print(id(well1))
# well1.plot(style={'color': 'dls'}).show()