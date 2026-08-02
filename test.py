from rayoptics.environment import *
import matplotlib.pyplot as plt

opm = OpticalModel()
sm  = opm['seq_model']
osp = opm['optical_spec']
pm = opm['parax_model']
em = opm['ele_model']
pt = opm['part_tree']
ar = opm['analysis_results']
osp.pupil = PupilSpec(osp, key=['image', 'f/#'], value=1.24)
osp.field_of_view = FieldSpec(osp, key=('object', 'angle'), value=31.65, flds=[0.0,0.7,1.0], is_relative=True, is_wide_angle=False)
osp.spectral_region = WvlSpec([(486.1327, 0.5), (587.5618, 1.0), (656.2725, 0.5)], ref_wl=1)
opm.system_spec.title = "US 2025/0271647 Example 2"
opm.system_spec.dimensions = 'mm'
opm.radius_mode = True
sm.gaps[0].thi=1e10
sm.add_surface([-45.14130257097362,1.75,1.59551,39.21],sd=17.18)
sm.add_surface([26.66682265149467,7.35,2.001,29.14],sd=15.13)
sm.add_surface([-130.9917091612707,0.35],sd=15.13)
sm.add_surface([42.02963060611184,7.0,1.7432,49.34],sd=14.09)
sm.ifcs[sm.cur_surface].profile = EvenPolynomial(r=42.02963060611184, cc=0.0,
	coefs=[0.0,-8.62921617782276E-6,-1.342558971929082E-8,-1.531947083630983E-11])
sm.add_surface([-28.1701844466078,1.4,1.7552,27.51],sd=13.48)
sm.add_surface([29.4692182045642,4.9],sd=12.17)
sm.add_surface([0.0,1.75],sd=12.236)
sm.set_stop()
sm.add_surface([0.0,5.6,1.883,40.77],sd=12.77)
sm.add_surface([-46.30545505257408,1.4,1.738,32.26],sd=12.77)
sm.add_surface([20.12057945420811,8.4,1.7432,49.34],sd=12.77)
sm.add_surface([-84.69250364918614,0.35],sd=12.77)
sm.ifcs[sm.cur_surface].profile = EvenPolynomial(r=-84.69250364918614, cc=0.0,
	coefs=[0.0,-2.261846981549454E-6,-1.018542454232524E-8,1.530069013720622E-11,6.691202976300796E-14])
sm.add_surface([26.8952212503084,7.0,1.95375,32.32],sd=12.07)
sm.add_surface([-34.57503522198205,1.4,1.64769,33.79],sd=11.68)
sm.add_surface([22.52864175656453,4.55],sd=11.51)
sm.add_surface([-64.54680580236648,2.1,1.92286,18.9],sd=11.51)
sm.add_surface([-103.3490119292906,13.41],sd=11.77)
sm.ifcs[sm.cur_surface].profile = EvenPolynomial(r=-103.3490119292906, cc=0.0,
	coefs=[0.0,2.847103618026058E-5,-3.275822424549171E-8,1.171196274655365E-9,-5.500563523310379E-12,1.234593736675926E-14])
sm.add_surface([0.0,0.75,1.51633,64.14],sd=25.67)
sm.add_surface([0.0,0.85],sd=25.67)
sm.list_surfaces()
sm.list_gaps()
sm.do_apertures = False
opm.update_model()
set_vignetting(opm)
print('')
listobj(osp)
layout_plt = plt.figure(FigureClass=InteractiveLayout, opt_model=opm, do_draw_rays=True, do_paraxial_layout=False,
                        is_dark=False).plot()
layout_plt.savefig("layout.svg", format="svg")