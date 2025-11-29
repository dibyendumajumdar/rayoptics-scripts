from rayoptics.environment import *
from rayoptics.elem.profiles import EvenPolynomial
from rayoptics.optical.opticalmodel import OpticalModel
from rayoptics.raytr.opticalspec import PupilSpec, FieldSpec, WvlSpec
from rayoptics.raytr import trace, wideangle, vigcalc

opm = OpticalModel()
sm  = opm['seq_model']
osp = opm['optical_spec']
fov = osp['fov']
pm = opm['parax_model']
em = opm['ele_model']
pt = opm['part_tree']
ar = opm['analysis_results']
osp['pupil'] = PupilSpec(osp, key=['image', 'f/#'], value=2.88)
#fov = osp['fov'] = FieldSpec(osp, key=['object', 'angle'], value=114.7/2, flds=[0., 0.7071, 1.0],
#                             is_relative=True, is_wide_angle=True)
fov = osp['fov'] = FieldSpec(osp, key=['object', 'angle'], value=114.7/2, flds=[1.0],
                             is_relative=True, is_wide_angle=True)
#osp['wvls'] = WvlSpec([(486.1327, 0.5), (587.5618, 1.0), (656.2725, 0.5)], ref_wl=1)
osp['wvls'] = WvlSpec([(587.5618, 1.0)], ref_wl=0)
opm.system_spec.title = "US 7,359,125 Example 1 (Nikon AF-S Nikkor 14-24mm f/2.8G ED)"
opm.system_spec.dimensions = 'MM'
opm.radius_mode = True
sm.gaps[0].thi=1e10
sm.add_surface([60.3937,3.5,'J-LASF015','Hikari'])
sm.ifcs[sm.cur_surface].max_aperture = 41.41
sm.add_surface([32.2703,7.0835])
sm.ifcs[sm.cur_surface].max_aperture = 31.01
sm.add_surface([35.5,4.0,'Q-LAK52S','Hikari'])
sm.ifcs[sm.cur_surface].max_aperture = 29.73
sm.add_surface([19.5117,12.8951])
sm.ifcs[sm.cur_surface].profile = EvenPolynomial(r=19.5117, cc=-0.9087,
	coefs=[0.0,-5.1181E-7,7.1056E-10,-1.9817E-11,1.9226E-14,-6.0945E-18,0.0,0.0])
sm.ifcs[sm.cur_surface].max_aperture = 25.89
sm.add_surface([87.0449,2.5,'J-LAK011','Hikari'])
sm.ifcs[sm.cur_surface].max_aperture = 25.09
sm.add_surface([26.3306,0.3,1.55389,38.09])
sm.ifcs[sm.cur_surface].max_aperture = 19.81
sm.add_surface([30.2448,12.6887])
sm.ifcs[sm.cur_surface].profile = EvenPolynomial(r=30.2448, cc=-7.3795,
	coefs=[0.0,4.2239E-5,-7.8972E-8,2.9788E-10,-5.9331E-13,6.0285E-16,-7.4037E-20,0.0])
sm.ifcs[sm.cur_surface].max_aperture = 19.775
sm.add_surface([-67.993,2.5896,'J-FKH1','Hikari'])
sm.ifcs[sm.cur_surface].max_aperture = 19.775
sm.add_surface([48.0626,2.0])
sm.ifcs[sm.cur_surface].max_aperture = 19.65
sm.add_surface([48.488,5.9634,'J-LASF013','Hikari'])
sm.ifcs[sm.cur_surface].max_aperture = 19.65
sm.add_surface([-181.2948,31.93])
sm.ifcs[sm.cur_surface].max_aperture = 19.65
sm.add_surface([34.6184,1.0,'J-LASF05','Hikari'])
sm.ifcs[sm.cur_surface].max_aperture = 12.07
sm.add_surface([19.4637,5.2931,'J-BAF8','Hikari'])
sm.ifcs[sm.cur_surface].max_aperture = 11.56
sm.add_surface([611.599,5.86])
sm.ifcs[sm.cur_surface].max_aperture = 11.56
sm.add_surface([0.0,1.6689])
sm.set_stop()
sm.ifcs[sm.cur_surface].max_aperture = 9.1645
#sm.add_surface([-265.5383,2.6545,'J-BK7','Hikari'])
sm.add_surface([-265.5383,2.6545,'J-BK7A','Hikari'])
sm.ifcs[sm.cur_surface].max_aperture = 11.86
sm.add_surface([-47.2569,9.0744])
sm.ifcs[sm.cur_surface].max_aperture = 11.86
sm.add_surface([-27.9322,1.6819,'J-LASF05','Hikari'])
sm.ifcs[sm.cur_surface].max_aperture = 11.76
sm.add_surface([138.6775,0.1])
sm.ifcs[sm.cur_surface].max_aperture = 11.76
#sm.add_surface([35.6745,4.4701,'BAFL2','Hoya'])
sm.add_surface([35.6745,4.4701,1.570989,50.858935])
sm.ifcs[sm.cur_surface].max_aperture = 12.27
sm.add_surface([-71.8719,0.1])
sm.ifcs[sm.cur_surface].max_aperture = 12.27
sm.add_surface([27.2079,1.3817,'J-LASF016','Hikari'])
sm.ifcs[sm.cur_surface].max_aperture = 12.58
sm.add_surface([16.4317,8.491,'J-FKH1','Hikari'])
sm.ifcs[sm.cur_surface].max_aperture = 12.17
sm.add_surface([-53.0,1.721])
sm.ifcs[sm.cur_surface].max_aperture = 12.17
sm.add_surface([1336.7107,1.0,'NBFD13','Hoya'])
sm.ifcs[sm.cur_surface].max_aperture = 12.48
sm.add_surface([20.3824,6.3537,'M-BACD5N','Hoya'])
sm.ifcs[sm.cur_surface].max_aperture = 12.48
sm.add_surface([-60.1135,38.58])
sm.ifcs[sm.cur_surface].profile = EvenPolynomial(r=-60.1135, cc=5.0164,
	coefs=[0.0,1.9855E-5,6.9569E-9,1.5384E-10,-5.8393E-13,0.0,0.0,0.0])
sm.ifcs[sm.cur_surface].max_aperture = 12.48
sm.list_surfaces()
sm.list_gaps()
sm.do_apertures = False
opm.update_model()
vigcalc.set_vig(opm, use_bisection=True)
opm.update_model()

def ray_abr(p, xy, ray_pkg, fld, wvl, foc):
    if ray_pkg[mc.ray] is not None:
        image_pt = fld.ref_sphere[0]
        ray = ray_pkg[mc.ray]
        dist = foc / ray[-1][mc.d][2]
        defocused_pt = ray[-1][mc.p] + dist * ray[-1][mc.d]
        t_abr = defocused_pt - image_pt
        return t_abr[xy]
    else:
        return None

result = sm.trace_fan(ray_abr,0,1, num_rays=21)

print(result[0])
print(result[1])

result = sm.trace_fan(ray_abr,0,0, num_rays=21)

print(result[0])
print(result[1])