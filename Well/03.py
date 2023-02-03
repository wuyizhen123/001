import wellbore_trajectories as wp
import torque_and_drag as tad

well = wp.load('trajectory2.xlsx', inner_points=5)
# well.plot(style={'color': 'dls'}).show()

bha = tad.architecture.BHA(name='xxxx', top=0, bottom=1458.2, method='bottom_up')
bha.add_section(od=0.2, id=0.159, length=267.76, unit_weight=512.54, name='1')
bha.add_section(od=0.1778, id=0.1594, length=1190.44, unit_weight=379.55, name='1')
# print(bha.sections)  # 加载管串数据并测试

wellbore = tad.architecture.WellBore(name='xxxx', top=0, bottom=1469, method='top_down')
wellbore.add_section(od=0.3397, id=0.31026, bottom=150, unit_weight=None, coeff_friction_sliding=0.25,name='xxx')
wellbore.add_section(od=None, id=0.2445, bottom=1469, unit_weight=None, coeff_friction_sliding=0.35, name='xx')
# print(wellbore.sections)

t_and_d = tad.torque_drag.TorqueDrag(well=well, wellbore=wellbore, string=bha, fluid_density=1.2, name='8 1/2" Hole Section')

# print(t_and_d.tension['slackoff'])
# print(t_and_d.tension['pickup'])
# print(t_and_d.tension['rotating'])

t_and_d.figure().show()

hookload = tad.torque_drag.HookLoad(well=well, wellbore=wellbore, string=bha, fluid_density=1.2, step=30, name='xxx',
                                    ff_range=(0.05, 0.35, 0.1))
hookload.figure().show()