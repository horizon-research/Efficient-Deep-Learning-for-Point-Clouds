import matplotlib.style
import matplotlib as mpl
mpl.style.use('classic')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import FuncFormatter
from matplotlib.patches import Ellipse
import numpy as np
import math
mpl.rcParams['legend.numpoints'] = 1
plt.rcParams["font.family"] = "Arial"
# matplotlib.rcParams['pdf.fonttype'] = 42
# matplotlib.rcParams['ps.fonttype'] = 42

##############################################################
#                     PCloud Arch PROJECT                    #
##############################################################


def PlotAcc():
    data = {
        "Orginal" : [90.76, 84.01, 91.53, 84.92, 71.26, 92.9, 92.6], 
        "Mesorasi": [89.91, 84.05, 91.45, 84.21, 72.49, 92.3, 93.2]
    }

    # initialize the array from the result first.
    names = ["Orginal", "Mesorasi"]

    x_axis = {
        "Orginal" : [1.0, 4.0, 7.0, 10.0, 13.0, 16.0, 19.0], 
        "Mesorasi": [2.0, 5.0, 8.0, 11.0, 14.0, 17.0, 20.0]
    }

    x_axis_ls =[1.5, 4.5, 7.5, 10.5, 13.5, 16.5, 19.5]

    plt.rc('font', size=16)
    ax = plt.figure(figsize=(8, 2.5)).add_subplot(111)
    ax.set_ylabel('Accuracy (%)', fontsize=16)
    # plt.xticks(rotation=60)
    plt.setp(ax.spines.values(), linewidth=2)
    p = [None, None, None, None]
    colors = ['#a6a6a6', '#88cc00']
    hatches = ['----', '\\\\\\', '///']

    for i in range(2):
        for j in range(len(data[names[i]])):
            ax.text(x_axis[names[i]][j], data[names[i]][j]+0.20, ("%.1f" % data[names[i]][j]),
                ha='center', va='bottom', fontsize=12)
        p[i] = ax.bar(x_axis[names[i]], data[names[i]], 1.0, align='center', color='#ffffff',\
                edgecolor=[colors[i]]*len(x_axis_ls), linewidth=1.5, hatch=hatches[i]);
        ax.bar(x_axis[names[i]], data[names[i]], 1.0, align='center', color='none',\
                edgecolor=['k']*len(x_axis_ls), linewidth=1.5);
    
    plt.subplots_adjust(left=0.1, bottom=0.25, right=0.98, top=0.85,
                wspace=0.2, hspace=0.2)
    plt.xticks(x_axis_ls, ["PointNet++ (c)", "PointNet++ (s)", 
        "DGCNN (c)", "DGCNN (s)", "F-PointNet", "LDGCNN", "DensePoint"], fontsize=15, rotation=15)
    ax.tick_params(axis="y",direction="in")
    ax.tick_params(axis="x",direction="in")
    
    ax.set_ylim(40, 100)
    ax.set_xlim(0, 21)
    ax.set_yticks([40, 60, 80, 100])
    ax.set_yticks(range(40, 100, 4), minor=True)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 0, length=4)
    plt.grid(color='grey', which='major', axis='y', linestyle='--')
    plt.legend((p[0][0], p[1][0]), ('Original','Mesorasi'), \
            bbox_to_anchor=(-0.01, 1.01, 1.0, .101), loc=3,
            ncol=3, mode="expand", borderaxespad=0.1, frameon=False, \
            prop={'size': 16}, handletextpad=0.1)
    ax.set_axisbelow(True)
    
    plt.savefig("pcloud_accuracy.pdf");


def ProfileSoftwareSpeedupEnergy():
    # initialize the array from the result first.
    overall_speedup = [[1.22, 1.12, 1.33, 1.06, 1.09, 1.50, 1.92, 1.32],
                       [1.85, 1.67, 1.32, 1.16, 1.80, 1.52, 1.92, 1.62]]

    overall_saving = [[18.06, 11.03, 24.96, 6.53, 8.54, 44.90, 85.94, 28.28],
                      [64.47, 69.50, 23.93, 18.60, 52.04, 44.90, 85.94, 51.13]]


    x_axis_ls = range(1, 9)
    plt.rc('font', size=10)
    ax = plt.figure(figsize=(6, 2.5)).add_subplot(111)
    ax.set_ylabel('Speedup', fontsize=14)
    ax2 = ax.twinx()
    ax2.set_ylabel('Energy\nReduction (%)', fontsize=14)
    
    plt.setp(ax.spines.values(), linewidth=1.5)
    p = [None, None, None, None]
    
    colors = ['#88cc00', '#a6a6a6']
    markercolors = ['#dc5739', '#8154D1', '#ae774c']
    hatches = ['/////', '----', '\\\\\\\\\\']
    markers = ['o', 'v']
    bar_size = 0.4

    ax.plot([0, 8], [1, 1], color='black', linestyle='--', lw=1.5)
    tmp_x = [x+1.20*0.4 for x in x_axis_ls]
    p[0] = ax.bar(tmp_x, overall_speedup[1], bar_size, align='center', color='#ffffff',\
            edgecolor=[colors[0]]*len(x_axis_ls), linewidth=1.5, hatch=hatches[0]);
    ax.bar(tmp_x, overall_speedup[1], bar_size, align='center', color='none',\
            edgecolor=['k']*len(x_axis_ls), linewidth=1);
    p[1] = ax2.plot(tmp_x, overall_saving[1], linestyle='none', color=markercolors[0],\
            linewidth=2, markeredgecolor='k', markeredgewidth=1,\
             marker=markers[0], markersize=14)
    tmp_x = [x+0.20*0.4 for x in x_axis_ls]
    p[2] = ax.bar(tmp_x, overall_speedup[0], bar_size, align='center', color='#ffffff',\
            edgecolor=[colors[1]]*len(x_axis_ls), linewidth=1.5, hatch=hatches[1]);
    ax.bar(tmp_x, overall_speedup[0], bar_size, align='center', color='none',\
            edgecolor=['k']*len(x_axis_ls), linewidth=1);
    p[3] = ax2.plot(tmp_x, overall_saving[0], linestyle='none', color=markercolors[1],\
            linewidth=2, markeredgecolor='k', markeredgewidth=1,\
             marker=markers[1], markersize=14)

    plt.subplots_adjust(left=0.10, bottom=0.18, right=0.85, top=0.78,
                        wspace=0.2, hspace=0.2)
    plt.xticks([1.25, 2.25, 3.25, 4.25, 5.25, 6.25, 7.25, 8.25], \
                ['PointNet++ (c)', 'PointNet++ (s)', 'DGCNN (c)', \
                'DGCNN (s)','F-PointNet', 'LDGCNN', 'DensePoint', 'AVG.'], rotation=20)

    ax.tick_params(axis="y",direction="in")

    plt.arrow(0.20, 125, 0.3, 0, head_width=0, head_length=0, fc='k',\
             ec='k', lw=1.5, clip_on = False)
    plt.arrow(0.20, 125, 0, -6, head_width=0.125, head_length=2.5, fc='k',\
             ec='k', lw=1.5, clip_on = False)
    plt.arrow(9.8, 125, -0.3, 0, head_width=0, head_length=0, fc='k',\
             ec='k', lw=1.5, clip_on = False)
    plt.arrow(9.8, 125, 0, -6, head_width=0.125, head_length=2.5, fc='k',\
             ec='k', lw=1.5, clip_on = False)
    # ax.text(0.35, 0.75, '1', fontsize=10, color='red', clip_on = False)

    ax.set_xlim(0.75, 8.85)
    ax2.set_xlim(0.75, 8.85)
    ax2.set_ylim(0, 100)
    ax2.set_yticks([0, 25, 50, 75, 100])
    ax.set_ylim(0, 2.0)
    ax.set_yticks([0.1*i for i in range(0, 20)], minor=True)
    ax.tick_params(axis = 'y', which = 'minor', labelsize = 0, length=4)
    ax2.set_yticks([5*i for i in range(0, 20)], minor=True)
    ax2.tick_params(axis = 'y', which = 'minor', labelsize = 0, length=4)
    
    ax.set_yticks([0, 0.5, 1, 1.5, 2.0])
    ax.tick_params(axis="x",direction="in",rotation=20)
    ax2.tick_params(axis="x",direction="in",rotation=20)
    plt.xticks(rotation=20)
    
    legend1 = plt.legend((p[2][0], p[0][0],  p[3][0], p[1][0]), \
            ('Ltd. Mesorasi (Speedup)', 'Mesorasi (Speedup)', 'Ltd. Mesorasi (Energy)', 'Mesorasi (Energy)'), \
            bbox_to_anchor=(-0.03, 1.01, 1.1, .101), loc=3,
            ncol=2, mode="expand", borderaxespad=0., frameon=False,  prop={'size': 12})

    # plt.legend((p[2][0], p[3][0]), \
    #         (', 'GPU+NPU (Energy)'), \
    #         bbox_to_anchor=(0., 1.01, 1., .101), loc=4,
    #         ncol=1, borderaxespad=0., frameon=False,  prop={'size': 12})
    # plt.gca().add_artist(legend1)

    ax.grid(color='grey', which='major', axis='y', linestyle='--')
    ax.set_axisbelow(True)
    ax2.set_axisbelow(True)
    
    plt.savefig("gpu_speedup_energy.pdf");


def OpsReduction():
    # initialize the array from the result first.
    data = [79.30, 68.34, 61.24, 44.32, 88.47]


    x_axis_ls = range(1, 6)
    plt.rc('font', size=14)
    ax = plt.figure(figsize=(4, 3)).add_subplot(111)
    ax.set_ylabel('MAC Ops\nReduction (%)', fontsize=16)
    ax.grid(color='grey', which='major', axis='y', linestyle='--')
    ax.set_axisbelow(True)
    
    plt.setp(ax.spines.values(), linewidth=1.5)
    colors = ['#40bf40', '#4d4dff']
    colors = ['#88cc00', '#a6a6a6']
    markercolors = ['#dc5739', '#8154D1', '#ae774c']
    hatches = ['/////', '\\\\\\\\\\', '----']
    markers = ['o', 'v']

    p = ax.bar(x_axis_ls, data, 0.5, align='center', color='#ffffff',\
            edgecolor=[colors[0]]*len(x_axis_ls), linewidth=1.5, hatch=hatches[0]);
    ax.bar(x_axis_ls, data, 0.5, align='center', color='none',\
            edgecolor=['k']*len(x_axis_ls), linewidth=1);

    # plt.xticks(x_axis_ls, ['#1','#2', '#3','#4','#5'])
    # ['PointNet\n(cls)', 'DGCNN\n(cls)', 'PointNet\n(seg)', 'DGCNN\n(seg)','F-Point\nNet++']
    ax.tick_params(axis="y",direction="in")

    plt.subplots_adjust(left=0.25, bottom=0.23, right=0.95, top=0.88,
                        wspace=0.1, hspace=0.1)

    ax.set_xlim(0.5, 5.50)
    ax.set_ylim(0, 100)
    plt.xticks(x_axis_ls, ['PointNet++ (c)', 'PointNet++ (s)', 'DGCNN (c)', \
                'DGCNN (s)','F-PointNet'], rotation=20, size=14) 
    
    plt.savefig("ops_reduction.pdf");


def TotalOps():
    # initialize the array from the result first.
    data = [ i/(1.0*10**9) for i in \
    [7034025984, 3112003104, 36733834240, \
     186526745600, 185725730816, 271232000003, 315962614784, 155307746816]]


    x_axis_ls = range(1, 9)
    plt.rc('font', size=14)
    ax = plt.figure(figsize=(4, 3.5)).add_subplot(111)
    ax.set_ylabel('MAC Ops (GOPS)', fontsize=16)
    ax.grid(color='grey', which='major', axis='y', linestyle='--')
    ax.set_axisbelow(True)
    ax.set_yscale('log')
    
    plt.setp(ax.spines.values(), linewidth=1.5)
    colors = ['#f59153', '#88cc00', '#a6a6a6']
    markercolors = ['#dc5739', '#8154D1', '#ae774c']
    hatches = ['/////', '\\\\\\\\\\', '----']
    markers = ['o', 'v']

    p1 = ax.bar(x_axis_ls, data, 0.5, align='center', color='#ffffff',\
            edgecolor=[colors[1]]*len(x_axis_ls), linewidth=1.5, hatch=hatches[0]);

    p2 = ax.bar(x_axis_ls[0:3], data[0:3], 0.5, align='center', color='#ffffff',\
            edgecolor=[colors[2]]*len(x_axis_ls[0:3]), linewidth=1.5, hatch=hatches[0]);
    ax.bar(x_axis_ls, data, 0.5, align='center', color='none',\
            edgecolor=['k']*len(x_axis_ls), linewidth=1);
    ax.plot([3.5, 3.5], [1, 1000], color='grey', linestyle='--', lw=1.5)

    # plt.xticks(x_axis_ls, ['#1','#2', '#3','#4','#5'])
    # ['PointNet\n(cls)', 'DGCNN\n(cls)', 'PointNet\n(seg)', 'DGCNN\n(seg)','F-Point\nNet++']
    ax.tick_params(axis="y",direction="in")

    plt.subplots_adjust(left=0.20, bottom=0.40, right=0.95, top=0.90,
                        wspace=0.1, hspace=0.1)

    ax.set_xlim(0.5, 8.50)
    ax.set_ylim(10**0, 10**3)
    plt.xticks(x_axis_ls, ['YOLOv2', 'AlexNet', 'ResNet-50', 'PointNet++ (c)', 'PointNet++ (s)', 'DGCNN (c)', \
                'DGCNN (s)','F-PointNet'], rotation=60, size=16) 

    plt.legend((p2[0], p1[0]), \
            ('CNN', 'Point Cloud'), \
            bbox_to_anchor=(0., 1.01, 1., .101), loc=3,
            ncol=2, mode="expand", borderaxespad=0., frameon=False,  prop={'size': 12})
    # plt.annotate("", xy=(0.5, 5), xycoords='data',
    #          xytext=(3.5, 5), textcoords='data',
    #          arrowprops=dict(arrowstyle="<->"))
    # ax.text(1.5, 5, 'CNN', fontsize=12, color='k')
    # plt.annotate("", xy=(3.5, 5), xycoords='data',
    #          xytext=(8.5, 5), textcoords='data',
    #          arrowprops=dict(arrowstyle="<->"))
    # ax.text(5.0, 5, 'Point Cloud', fontsize=12, color='k')
    
    plt.savefig("mac_ops.pdf");


def PlotLayerOps():
    data1 = [sorted([49152,1048576,1048576,1073152,1048576,1048576, 2097152, 2097152]),
            sorted([98304,2097152,2097152,1048576,1048576,1048576, 2621440]),
            sorted([122880,1310720,122880,2621440,2621440,2621440,4194304,2097152]),
            sorted([360000,3840000,360000,3840000,7680000,3840000,7680000, 7680000]),
            sorted([16384,131072,131072,32768,524288,524288,65536,1048576, \
             1572864,655360,131072,131072,655360,262144,262144,1310720,524288,524288])]


    data2 = [sorted([3072,65536,65536,67072,65536,65536, 131072, 131072]),
            sorted([3072,131072,131072,65536,65536,65536, 131072]),
            sorted([6144,65536,6144,131072,131072,131072,131072, 65536]),
            sorted([18000,192000,18000,192000,384000,192000,384000,384000]),
            sorted([4096,32768,32768,4096,65536,65536,4096,65536,98304,40960,\
                    8192,8192,40960,16384,16384,40960,16384,16384])]

    for i in range(len(data1)):
        for j in range(len(data1[i])):
            data1[i][j] /= 256*1024.0
            data2[i][j] /= 256*1024.0


    plt.rc('font', size=14)
    ax = plt.figure(figsize=(4, 3)).add_subplot(111)
    plt.setp(ax.spines.values(), linewidth=1.5)

    ax.set_yscale('log', basey=2)
    ax.grid(color='grey', which='major', axis='y', linestyle='--')
    ax.set_ylabel('Data Size (MB)', fontsize=16)

    p1 = ax.violinplot(data1,[1.1,3.1,5.1,7.1,9.1])
    p2 = ax.violinplot(data2,[1.9,3.9,5.9,7.9,9.9])

    # Make all the violin statistics marks red:
    for partname in ('cbars','cmins','cmaxes',):
        vp = p2[partname]
        vp.set_edgecolor('#1515d1')

    for e in p2['bodies']:
        e.set_facecolor('#40bf40')

    # pc.set_edgecolor()
    ax.set_xlim(0.5, 10.5)
    ax.set_ylim(1.0/512, 2**6)

    plt.legend((p1['bodies'][0], p2['bodies'][0]), ('Original', 'Delayed-Aggr.'), \
            bbox_to_anchor=(-0.05, 1.01, 1., .101), loc=3,
            ncol=2, mode="expand", borderaxespad=0.1, frameon=False, \
            prop={'size': 14}, handletextpad=0.1)
    plt.subplots_adjust(left=0.18, bottom=0.23, right=0.95, top=0.88,
                        wspace=0.1, hspace=0.1)

    plt.xticks([1.5,3.5,5.5,7.5,9.5], ['PointNet++ (c)', 'PointNet++ (s)', 'DGCNN (c)', \
                'DGCNN (s)','F-PointNet'], rotation=20, size=14) 
    # plt.xticks([1.5,3.5,5.5,7.5,9.5], ['#1','#2', '#3','#4','#5'])
    # plt.minorticks_on()
    ax.set_yticks([1.0/512*2**i for i in range(0, 15)], minor=True)
    ax.tick_params(axis = 'both', which = 'minor', labelsize = 0)
    ax.set_yticks([1.0/512, 1.0/64, 1.0/8, 1, 8, 64])
    plt.yticks([1.0/512, 1.0/64, 1.0/8, 1, 8, 64], size=16)
    
    # ax.tick_params(axis = 'both', which = 'major', labelsize = 4)
    # ax.grid(color='grey', which='major', axis='y', linestyle='--')
    plt.savefig("layer_ops.pdf");

def PlotPointNet():
    # initialize the array from the result first.
    names = ["Orginal", "Mesorasi"]

    x_axis = {
        "Orginal" : [1.0, 4.0, 7.0], 
        "Mesorasi": [2.0, 5.0, 8.0]
    }

    data = {
        "Orginal" : [9.82, 0.85, 24.90], 
        "Mesorasi": [9.49, 3.86, 7.84]
    }

    x_axis_ls =[1.5, 4.5, 7.5]
    plt.rc('font', size=14)
    ax = plt.figure(figsize=(4, 3)).add_subplot(111)
    ax.set_ylabel('Time (msec.)', fontsize=16)
    # plt.xticks(rotation=60)
    plt.setp(ax.spines.values(), linewidth=1.5)
    p = [None, None, None, None]
    colors = ['#a6a6a6', '#88cc00']
    hatches = ['----', '\\\\\\', '///', '|||']

    for i in range(2):
        for j in range(len(data[names[i]])):
            ax.text(x_axis[names[i]][j], data[names[i]][j]+0.20, ("%.1f" % data[names[i]][j]),
                ha='center', va='bottom', fontsize=12)
        p[i] = ax.bar(x_axis[names[i]], data[names[i]], 1.0, align='center', color='#ffffff',\
                edgecolor=[colors[i]]*len(x_axis_ls), linewidth=1.5, hatch=hatches[i]);
        ax.bar(x_axis[names[i]], data[names[i]], 1.0, align='center', color='none',\
                edgecolor=['k']*len(x_axis_ls), linewidth=1.5);
        plt.errorbar(x_axis[names[i]], data[names[i]], yerr=[0.3*i for i in data[names[i]]],\
                    linestyle='none', linewidth=2.0)
    
    plt.subplots_adjust(left=0.20, bottom=0.23, right=0.95, top=0.88,
                wspace=0.1, hspace=0.1)
    plt.xticks(x_axis_ls, ["Neighbor\nSearch", "Aggregation", "Feature\nExtraction"], size=14)
    ax.tick_params(axis="y",direction="in")
    ax.tick_params(axis="x",direction="in")

    # ax.set_yscale('log')
    # plt.annotate("DCO", xy=(2.0, 3.5), xycoords='data',
    #          xytext=(1.0, 5.0), textcoords='data',
    #          arrowprops=dict(arrowstyle="->"))
    
    ax.set_ylim(0, 30)
    ax.set_xlim(0, 9)
    plt.grid(color='grey', which='major', axis='y', linestyle='--')
    plt.legend((p[0][0], p[1][0]), ('Original','Delayed-Aggr.'), \
            bbox_to_anchor=(-0.05, 1.01, 1.1, .101), loc=3,
            ncol=2, mode="expand", borderaxespad=0.1, frameon=False, \
            prop={'size': 14}, handletextpad=0.1)
    ax.set_axisbelow(True)
    
    plt.savefig("pointnet_dist.pdf");

def PlotTimeDist():
    # initialize the array from the result first.
    names = ["Orginal", "Mesorasi"]

    x_axis1 = [1, 4, 7, 10, 13, 16]
    x_axis2 = [2, 5, 8, 11, 14, 17]

    data1 = [1.26, 0.85, 3.29, 10.41, 2.22, 3.61]
    data2 = [3.61, 3.85, 4.89, 15.24, 7.29, 6.98]

    plt.rc('font', size=12)
    ax = plt.figure(figsize=(7, 2.5)).add_subplot(111)
    ax.set_ylabel('Time (msec.)', fontsize=16)
    ax2 = ax.twinx()
    ax2.set_ylabel('Relative Time (%)', fontsize=16)

    # plt.xticks(rotation=60)
    plt.setp(ax.spines.values(), linewidth=1.5)

    colors = ['#a6a6a6', '#88cc00']
    markercolors = ['#8154D1', '#dc5739', '#ae774c']
    hatches = [ '----', '/////', '\\\\\\\\\\',]
    markers = ['v', 'o']
    plt.grid(color='grey', which='major', axis='y', linestyle='--')

    plt.annotate("10.4", xy=(10, 40.0), xycoords='data',
             xytext=(8, 35.0), textcoords='data',
             arrowprops=dict(arrowstyle="->"))
    plt.annotate("15.2", xy=(11, 40.0), xycoords='data',
             xytext=(12, 35.0), textcoords='data',
             arrowprops=dict(arrowstyle="->"))

    org_group = ax.bar(x_axis1, data1, \
                1.0, align='center', color='#ffffff', \
                edgecolor=['#a6a6a6']*len(x_axis1), linewidth=1.5, hatch=hatches[0]);
    ax.bar(x_axis1, data1, \
            1.0, align='center', color='none',\
            edgecolor=['k']*len(x_axis1), linewidth=1);

    new_group = ax.bar(x_axis2, data2, \
                1.0, align='center', color='#ffffff',\
                edgecolor=['#88cc00']*len(x_axis1), linewidth=1.5, hatch=hatches[1]);

    ax.bar(x_axis2, data2, \
            1.0, align='center', color='none',\
            edgecolor=['k']*len(x_axis1), linewidth=1);

    org_pct = ax2.plot([1, 4, 7, 10, 13, 16], [5.8, 1.4, 3.9, 3.3, 4.0, 3.68], \
            linestyle='none', color='#8154D1',\
            linewidth=2, markeredgecolor='k', markeredgewidth=1,\
             marker='^', markersize=16)

    # [30.7, 10.9, 21.3, 5.6, 23.8]
    new_pct = ax2.plot([2, 5, 8, 11, 14, 17], [35.3, 33.8, 13.8, 7.7, 28.4, 23.8], \
            linestyle='none', color='#dc5739',\
            linewidth=2, markeredgecolor='k', markeredgewidth=1,\
             marker='o', markersize=14)

    plt.subplots_adjust(left=0.12, bottom=0.15, right=0.90, top=0.75,
                wspace=0.2, hspace=0.2)
    ax.tick_params(axis="y",direction="in", size=8)
    ax.tick_params(axis="x",direction="in")
    ax.set_ylim(1/10.0, 10)
    ax2.set_xlim(0, 18)
    ax2.set_ylim(0, 40)
    ax2.set_yticks([0, 20, 40])

    ax.set_yscale('log')

    plt.arrow(-1.3, 52, 0.3, 0, head_width=0, head_length=0, fc='k',\
             ec='k', lw=1.5, clip_on = False)
    plt.arrow(-1.3, 52, 0, -6, head_width=0.125, head_length=2.5, fc='k',\
             ec='k', lw=1.5, clip_on = False)
    plt.arrow(18.3, 52, -0.3, 0, head_width=0, head_length=0, fc='k',\
             ec='k', lw=1.5, clip_on = False)
    plt.arrow(18.3, 52, 0, -6, head_width=0.125, head_length=2.5, fc='k',\
             ec='k', lw=1.5, clip_on = False)
 
    plt.legend((org_group[0], new_group[0], org_pct[0], new_pct[0]), \
            ('Original','Delay-Aggr.', 'Original','Delay-Aggr.'), \
            bbox_to_anchor=(0.0, 1.01, 1.0, .101), loc=3,
            ncol=2, mode="expand", borderaxespad=0.1, frameon=False, \
            prop={'size': 14}, handletextpad=0.1)

    # ax.set_axisbelow(True)
    plt.xticks([1.5, 4.5, 7.5, 10.5, 13.5, 16.5], \
                ['PointNet++\n(c)', 'PointNet++\n(s)', 'DGCNN\n(c)', \
                'DGCNN\n(s)','F-PointNet', 'AVG.'])

    plt.savefig("runtime_dist.pdf");


def ProfileHardwareEnergy():

    overall_saving = [[4.72, 2.95, 2.00, 1.32, 3.59, 1.99, 1.41, 2.57],
                    [0.98, 0.98, 0.81, 0.84, 0.98, 0.72, 0.16, 0.78],
                    [0.69, 0.82, 0.69, 0.78, 0.65, 0.63, 0.07, 0.62]]

    x_axis_ls = range(1, 9)
    plt.rc('font', size=10)
    ax = plt.figure(figsize=(6, 2)).add_subplot(111)
    ax.set_ylabel('Norn. Energy', fontsize=14)
    
    plt.setp(ax.spines.values(), linewidth=1.5)
    p = [None, None, None, None]
    
    colors = ['#f59153', '#a6a6a6', '#88cc00']
    markercolors = ['#ae774c', '#8154D1', '#dc5739']
    hatches = ['\\\\\\\\\\', '----', '/////', ]
    markers = ['v', 'o']


    tmp_x = [x+0.1 for x in x_axis_ls]
    # ax.text(1.1, 3.05, ("4.7"), ha='center', va='bottom', fontsize=14, color='r')
    # ax.text(5.1, 3.05, ("3.6"), ha='center', va='bottom', fontsize=14, color='r')
    plt.annotate("4.7", xy=(1.1, 3.0), xycoords='data',
             xytext=(1.5, 2.4), textcoords='data',
             arrowprops=dict(arrowstyle="->"))
    plt.annotate("3.6", xy=(5.1, 3.0), xycoords='data',
             xytext=(5.5, 2.4), textcoords='data',
             arrowprops=dict(arrowstyle="->"))

    p[0] = ax.bar(tmp_x, overall_saving[0], 0.25, align='center', color='#ffffff',\
            edgecolor=[colors[0]]*len(x_axis_ls), linewidth=1.5, hatch=hatches[0]);
    ax.bar(tmp_x, overall_saving[0], 0.25, align='center', color='none',\
            edgecolor=['k']*len(x_axis_ls), linewidth=1);

    tmp_x = [x+0.35 for x in x_axis_ls]
    p[1] = ax.bar(tmp_x, overall_saving[1], 0.25, align='center', color='#ffffff',\
            edgecolor=[colors[1]]*len(x_axis_ls), linewidth=1.5, hatch=hatches[1]);
    ax.bar(tmp_x, overall_saving[1], 0.25, align='center', color='none',\
            edgecolor=['k']*len(x_axis_ls), linewidth=1);

    tmp_x = [x+0.6 for x in x_axis_ls]
    p[2] = ax.bar(tmp_x, overall_saving[2], 0.25, align='center', color='#ffffff',\
            edgecolor=[colors[2]]*len(x_axis_ls), linewidth=1.5, hatch=hatches[2]);
    ax.bar(tmp_x, overall_saving[2], 0.25, align='center', color='none',\
            edgecolor=['k']*len(x_axis_ls), linewidth=1);

    ax.plot([0, 10], [1, 1], color='red', linestyle='--', lw=1.5)

    plt.subplots_adjust(left=0.07, bottom=0.23, right=0.98, top=0.85,
                        wspace=0.2, hspace=0.2)

    plt.xticks([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5], \
                ['PointNet++ (c)', 'PointNet++ (s)', 'DGCNN (c)', \
                'DGCNN (s)','F-PointNet', 'LDGCNN', 'DensePoint', 'AVG.'], rotation=20)

    plt.annotate("Our Baseline", xy=(3.7, 1.0), xycoords='data',
             xytext=(3.7, 2.4), textcoords='data',
             arrowprops=dict(arrowstyle="->"))

    plt.yticks(range(6))
    ax.tick_params(axis="y",direction="in")
    ax.set_xlim(0.75, 9.0)
    ax.set_ylim(0, 3)
    ax.set_yticks([0.2*i for i in range(0, 15)], minor=True)
    ax.tick_params(axis = 'y', which = 'minor', labelsize = 0, length=4)
    
    legend1 = plt.legend((p[0][0], p[1][0], p[2][0]), \
            ('GPU', 'Mesorasi-SW', 'Mesorasi-HW'), \
            bbox_to_anchor=(0.0, 1.0, 1.0, .1), loc=3,
            ncol=3, mode="expand", borderaxespad=0., frameon=False,  prop={'size': 12})

    ax.grid(color='grey', which='major', axis='y', linestyle='--')
    ax.set_axisbelow(True)
    # ax2.set_axisbelow(True)
    
    plt.savefig("hw_energy.pdf");

def ProfileHardwareSpeedup():
    # initialize the array from the result first.
    overall_speedup = [[0.37, 0.42, 0.56, 0.81, 0.36, 0.59, 0.75, 0.55],
                        [1.19, 1.14, 1.40, 1.21, 1.15, 1.42, 1.78, 1.33],
                        [2.20, 1.50, 1.62, 1.28, 1.42, 1.57, 3.57, 1.88]]
    limit = 2

    x_axis_ls = range(1, 9)
    plt.rc('font', size=10)
    ax = plt.figure(figsize=(6, 2)).add_subplot(111)
    ax.set_ylabel('Speedup', fontsize=14)
    # ax2 = ax.twinx()
    # ax2.set_ylabel('Energy\nReduction (%)', fontsize=14)
    
    
    plt.setp(ax.spines.values(), linewidth=1.5)
    p = [None, None, None, None]
    
    colors = ['#f59153', '#a6a6a6', '#88cc00']
    markercolors = ['#ae774c', '#8154D1', '#dc5739']
    hatches = ['\\\\\\\\\\', '----', '/////', ]
    markers = ['v', 'o']

    ax.plot([0, 9], [1, 1], color='red', linestyle='--', lw=1.5)

    tmp_x = [x+0.1 for x in x_axis_ls]
    p[0] = ax.bar(tmp_x, overall_speedup[0], 0.25, align='center', color='#ffffff',\
            edgecolor=[colors[0]]*len(x_axis_ls), linewidth=1.5, hatch=hatches[0]);
    ax.bar(tmp_x, overall_speedup[0], 0.25, align='center', color='none',\
            edgecolor=['k']*len(x_axis_ls), linewidth=1);

    tmp_x = [x+0.35 for x in x_axis_ls]
    p[1] = ax.bar(tmp_x, overall_speedup[1], 0.25, align='center', color='#ffffff',\
            edgecolor=[colors[1]]*len(x_axis_ls), linewidth=1.5, hatch=hatches[1]);
    ax.bar(tmp_x, overall_speedup[1], 0.25, align='center', color='none',\
            edgecolor=['k']*len(x_axis_ls), linewidth=1);

    tmp_x = [x+0.60 for x in x_axis_ls]
    # ax.text(1.6, 2.04, ("2.2"), ha='center', va='bottom', fontsize=14, color='r')
    plt.annotate("2.2", xy=(1.6, 2.0), xycoords='data',
             xytext=(2.0, 1.7), textcoords='data',
             arrowprops=dict(arrowstyle="->"))
    plt.annotate("3.6", xy=(7.6, 2.0), xycoords='data',
             xytext=(8.0, 1.7), textcoords='data',
             arrowprops=dict(arrowstyle="->"))

    p[2] = ax.bar(tmp_x, overall_speedup[2], 0.25, align='center', color='#ffffff',\
            edgecolor=[colors[2]]*len(x_axis_ls), linewidth=1.5, hatch=hatches[2]);
    ax.bar(tmp_x, overall_speedup[2], 0.25, align='center', color='none',\
            edgecolor=['k']*len(x_axis_ls), linewidth=1);

    plt.annotate("Our Baseline", xy=(5.8, 1.0), xycoords='data',
             xytext=(5.8, 1.7), textcoords='data',
             arrowprops=dict(arrowstyle="->"))

    plt.subplots_adjust(left=0.07, bottom=0.23, right=0.98, top=0.85,
                        wspace=0.2, hspace=0.2)

    plt.xticks([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5], \
                ['PointNet++ (c)', 'PointNet++ (s)', 'DGCNN (c)', \
                'DGCNN (s)','F-PointNet', 'LDGCNN', 'DensePoint', 'AVG.'], rotation=20)

    ax.tick_params(axis="y",direction="in")

    ax.set_xlim(0.75, 9.0)
    ax.set_ylim(0, limit)
    ax.set_yticks(range(limit+1))
    ax.set_yticks([0.1*limit*i for i in range(0, 10)], minor=True)
    ax.tick_params(axis = 'y', which = 'minor', labelsize = 0, length=4)

    legend1 = plt.legend((p[0][0], p[1][0], p[2][0]), \
            ('GPU', 'Mesorasi-SW', 'Mesorasi-HW'), \
            bbox_to_anchor=(0.0, 1.0, 1.0, .1), loc=3,
            ncol=3, mode="expand", borderaxespad=0., frameon=False,  prop={'size': 12})


    ax.grid(color='grey', which='major', axis='y', linestyle='--')
    ax.set_axisbelow(True)
    # ax2.set_axisbelow(True)
    
    plt.savefig("hw_speedup.pdf")


def ProfileNSESpeedup():

    overall_speedup = [[0.23, 0.17, 0.23, 0.19, 0.18, 0.22, 0.57, 0.26],
                        [1.13, 1.16, 2.65, 2.42, 1.24, 3.43, 2.34, 2.05],
                        [3.71, 3.06, 7.14, 5.07, 2.08, 8.01, 17.89, 6.71]]
    limit = 10

    x_axis_ls = range(1, 9)
    plt.rc('font', size=10)
    ax = plt.figure(figsize=(6, 2)).add_subplot(111)
    ax.set_ylabel('Speedup', fontsize=14)
    # ax2 = ax.twinx()
    # ax2.set_ylabel('Energy\nReduction (%)', fontsize=14)
    # ax.text(1.6, 2.04, ("2.2"), ha='center', va='bottom', fontsize=14, color='r')
    # plt.annotate("7.1", xy=(3.6, 5.0), xycoords='data',
    #          xytext=(3.9, 4.2), textcoords='data',
    #          arrowprops=dict(arrowstyle="->"))
    # plt.annotate("5.1", xy=(4.6, 5.0), xycoords='data',
    #          xytext=(4.9, 4.2), textcoords='data',
    #          arrowprops=dict(arrowstyle="->"))

    plt.annotate("17.9", xy=(7.6, 10.0), xycoords='data',
             xytext=(7.9, 8.2), textcoords='data',
             arrowprops=dict(arrowstyle="->"))
    
    
    plt.setp(ax.spines.values(), linewidth=1.5)
    p = [None, None, None, None]
    
    colors = ['#f59153', '#a6a6a6', '#88cc00']
    markercolors = ['#ae774c', '#8154D1', '#dc5739']
    hatches = ['\\\\\\\\\\', '----', '/////', ]
    markers = ['v', 'o']

    ax.plot([0, 10], [1, 1], color='red', linestyle='--', lw=1.5)

    tmp_x = [x+0.1 for x in x_axis_ls]
    p[0] = ax.bar(tmp_x, overall_speedup[0], 0.25, align='center', color='#ffffff',\
            edgecolor=[colors[0]]*len(x_axis_ls), linewidth=1.5, hatch=hatches[0]);
    ax.bar(tmp_x, overall_speedup[0], 0.25, align='center', color='none',\
            edgecolor=['k']*len(x_axis_ls), linewidth=1);

    tmp_x = [x+0.35 for x in x_axis_ls]
    p[1] = ax.bar(tmp_x, overall_speedup[1], 0.25, align='center', color='#ffffff',\
            edgecolor=[colors[1]]*len(x_axis_ls), linewidth=1.5, hatch=hatches[1]);
    ax.bar(tmp_x, overall_speedup[1], 0.25, align='center', color='none',\
            edgecolor=['k']*len(x_axis_ls), linewidth=1);

    tmp_x = [x+0.60 for x in x_axis_ls]
    
    p[2] = ax.bar(tmp_x, overall_speedup[2], 0.25, align='center', color='#ffffff',\
            edgecolor=[colors[2]]*len(x_axis_ls), linewidth=1.5, hatch=hatches[2]);
    ax.bar(tmp_x, overall_speedup[2], 0.25, align='center', color='none',\
            edgecolor=['k']*len(x_axis_ls), linewidth=1);

    # plt.annotate("Our Baseline", xy=(5.0, 1.0), xycoords='data',
    #          xytext=(5.0, 2.8), textcoords='data',
    #          arrowprops=dict(arrowstyle="->"))

    plt.subplots_adjust(left=0.07, bottom=0.23, right=0.98, top=0.85,
                        wspace=0.2, hspace=0.2)

    plt.xticks([1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5], \
                ['PointNet++ (c)', 'PointNet++ (s)', 'DGCNN (c)', \
                'DGCNN (s)','F-PointNet', 'LDGCNN', 'DensePoint', 'AVG.'], rotation=20)


    ax.tick_params(axis="y",direction="in")

    ax.set_xlim(0.75, 9.0)
    ax.set_ylim(0, limit)
    ax.set_yticks(range(0, limit+1, 2))
    ax.set_yticks([0.1*limit*i for i in range(0, 9)], minor=True)
    ax.tick_params(axis = 'y', which = 'minor', labelsize = 0, length=4)

    legend1 = plt.legend((p[0][0], p[1][0], p[2][0]), \
            ('GPU', 'Mesorasi-SW', 'Mesorasi-HW'), \
            bbox_to_anchor=(0.0, 1.0, 1.0, .1), loc=3,
            ncol=3, mode="expand", borderaxespad=0., frameon=False,  prop={'size': 12})


    ax.grid(color='grey', which='major', axis='y', linestyle='--')
    ax.set_axisbelow(True)
    # ax2.set_axisbelow(True)
    
    # plt.savefig("hw_speedup.pdf");
    plt.savefig("nse_speedup.pdf");


def SystolicArraySpeedUp():
    # initialize the array from the result first.
    data = [4.90, 3.36, 2.67, 1.92, 8.12, 4.35, 9.97, 5.08]
    overall_saving = [79.66, 71.69, 69.75, 59.79, 84.88, 79.24, 89.38, 76.34]


    x_axis_ls = range(1, 9)
    plt.rc('font', size=16)
    ax = plt.figure(figsize=(4, 3)).add_subplot(111)
    ax.set_ylabel('Speedup', fontsize=16)
    ax2 = ax.twinx()
    ax2.set_ylabel('Energy Reduction (%)', fontsize=16)
    ax.grid(color='grey', which='major', axis='y', linestyle='--')
    ax.set_axisbelow(True)
    
    plt.setp(ax.spines.values(), linewidth=1.5)
    markers = ['o', 'v']

    p1 = ax.bar(x_axis_ls, data, 0.5, align='center', color='#ffffff',\
            edgecolor=['#88cc00']*len(x_axis_ls), linewidth=1.5, hatch='/////');
    ax.bar(x_axis_ls, data, 0.5, align='center', color='none',\
            edgecolor=['k']*len(x_axis_ls), linewidth=1);
    p2 = ax2.plot(x_axis_ls, overall_saving, linestyle='none', color='#dc5739',\
            linewidth=2, markeredgecolor='k', markeredgewidth=1,\
             marker='o', markersize=14)

    ax.tick_params(axis="y",direction="in")

    plt.subplots_adjust(left=0.15, bottom=0.40, right=0.80, top=0.88,
                        wspace=0.1, hspace=0.1)

    plt.legend((p1[0], p2[0]), ('Speedup', 'Energy'), \
            bbox_to_anchor=(-0.05, 1.03, 1.1, .101), loc=3,
            ncol=2, mode="expand", borderaxespad=0., frameon=False,  prop={'size': 14})


    ax.set_xlim(0.5, 8.50)
    ax.set_ylim(0, 10)
    ax2.set_ylim(0, 100)
    ax.set_xticks([i-0.5 for i in range(1, 9)])
    ax.set_xticklabels(['PointNet++ (c)', 'PointNet++ (s)', 'DGCNN (c)', \
                'DGCNN (s)','F-PointNet', 'LDGCNN', 'DensePoint', '      AVG.   '], rotation=60, size=14)
    
    plt.savefig("systolic_speedup.pdf");

def GroupSpeedUp():
    # initialize the array from the result first.
    data = [6.57, 6.28, 12.49, 7.73, 1.80, 8.94, 8.81, 7.51]
    overall_saving = [99] * 8


    x_axis_ls = range(1, 9)
    plt.rc('font', size=16)
    ax = plt.figure(figsize=(4, 3)).add_subplot(111)
    ax.set_ylabel('Speedup', fontsize=16)
    ax2 = ax.twinx()
    ax2.set_ylabel('Energy Reduction (%)', fontsize=16)
    ax.grid(color='grey', which='major', axis='y', linestyle='--')
    ax.set_axisbelow(True)
    
    plt.setp(ax.spines.values(), linewidth=1.5)
    markers = ['o', 'v']

    p1 = ax.bar(x_axis_ls, data, 0.5, align='center', color='#ffffff',\
            edgecolor=['#88cc00']*len(x_axis_ls), linewidth=1.5, hatch='/////');
    ax.bar(x_axis_ls, data, 0.5, align='center', color='none',\
            edgecolor=['k']*len(x_axis_ls), linewidth=1);
    p2 = ax2.plot(x_axis_ls, overall_saving, linestyle='none', color='#dc5739',\
            linewidth=2, markeredgecolor='k', markeredgewidth=1,\
             marker='o', markersize=14)

    ax.tick_params(axis="y",direction="in")

    plt.subplots_adjust(left=0.15, bottom=0.40, right=0.80, top=0.88,
                        wspace=0.1, hspace=0.1)

    plt.legend((p1[0], p2[0]), ('Speedup', 'Energy'), \
            bbox_to_anchor=(-0.05, 1.03, 1.1, .101), loc=3,
            ncol=2, mode="expand", borderaxespad=0., frameon=False,  prop={'size': 14})

    ax.set_xlim(0.5, 8.50)
    ax.set_ylim(0, 15)
    ax.set_yticks([0, 3, 6, 9, 12, 15])
    ax2.set_ylim(0, 100)
    ax.set_xticks([i-0.5 for i in range(1, 9)])
    ax.set_xticklabels(['PointNet++ (c)', 'PointNet++ (s)', 'DGCNN (c)', \
                'DGCNN (s)','F-PointNet', 'LDGCNN', 'DensePoint', '      AVG.   '], rotation=60, size=14)
    
    plt.savefig("group_speedup.pdf");



def SystolicArrayProfile():
    # initialize the array from the result first.
    speedup = [[3.26, 3.37, 3.40, 3.68, 3.71, 3.76],
                [2.75, 1.51, 1.29, 1.20, 1.19, 1.19]]
    energy = [[0.29, 0.28, 0.28, 0.27, 0.27, 0.27],
                [0.82, 0.82, 0.81, 0.81, 0.79, 0.77]]


    x_axis_ls = [ i+0.5 for i in range(1, 7)]
    plt.rc('font', size=16)
    ax = plt.figure(figsize=(4, 3)).add_subplot(111)
    ax.set_ylabel('Speedup', fontsize=16)
    ax.set_xlabel('SA Size', fontsize=16)
    ax2 = ax.twinx()
    ax2.set_ylabel('Norm. Energy', fontsize=16)
    ax.grid(color='grey', which='major', axis='y', linestyle='--')
    ax.set_axisbelow(True)
    
    plt.setp(ax.spines.values(), linewidth=1.5)
    markers = ['o', 'v']

    # p1 = ax.plot(x_axis_ls, speedup[0], linestyle='--', color='#bf5aed', linewidth=1.5,
    #     markeredgecolor='k', markeredgewidth=1, marker='^', markersize=8)
    p2 = ax.plot(x_axis_ls, speedup[1], color='#88cc00', linewidth=1.5, 
        markeredgecolor='k', markeredgewidth=1, marker='^', markersize=14)
    # p3 = ax2.plot(x_axis_ls,energy[0], linestyle='--', color='#bdd3ff', linewidth=1.5,
    #         markeredgecolor='k', markeredgewidth=1, marker='o', markersize=8)
    p4 = ax2.plot(x_axis_ls,energy[1], color='#f59153', linewidth=2, \
            markeredgecolor='k', markeredgewidth=1, marker='o', markersize=14)
    # markeredgewidth=1,marker='o', markersize=14)

    ax.tick_params(axis="y",direction="in")

    plt.subplots_adjust(left=0.18, bottom=0.22, right=0.83, top=0.85,
                        wspace=0.1, hspace=0.1)

    plt.legend((p2[0], p4[0]), ('Speedup', 'Energy'), \
            bbox_to_anchor=(-0.05, 1.03, 1.1, .101), loc=3,
            ncol=2, mode="expand", borderaxespad=0., frameon=False,  prop={'size': 14})

    ax.set_xlim(1, 7)
    ax.set_ylim(0, 3)
    ax2.set_ylim(0.4, 1)
    ax.set_xticks(x_axis_ls)
    ax.set_xticklabels(['8x8', '16x16', '24x24', '32x32','40x40', '48x48'], rotation=20, size=14)
    
    plt.savefig("systolic_profile.pdf");

def profile_au():
    y = ["8", "16", "32", "64", "128", "256"]
    x = ["3", "6", "12", "24", "48", "96"]

    # Flow-Net-C
    res = np.array([[31.77, 15.89, 7.95, 4.10, 2.17, 2.17],
                    [15.89, 7.95, 3.98, 2.05, 1.09, 1.09],
                    [7.95, 3.98, 1.99, 1.03, 0.55, 0.55],
                    [3.98, 1.99, 1.00, 0.52, 0.28, 0.28],
                    [1.99, 1.00, 0.50, 0.26, 0.14, 0.14],
                    [1.00, 0.50, 0.26, 0.14, 0.08, 0.08]])

    # print(res)
    res = np.array(res)
    fig, ax = plt.subplots()
    ax.set_xlabel('NIT Buffer Size (KB)', fontsize=32)
    ax.set_ylabel('PFT Buffer Size (KB)', fontsize=32)
    plt.rc('font', size=32)
    plt.tick_params(axis='both', which='major', labelsize=32)
    im, cbar = heatmap(res, y, x, ax=ax, 
                   cmap=cmap_name, cbarlabel="Norm. Energy",
                   norm=matplotlib.colors.Normalize(vmin=0, vmax=4))

    texts = annotate_heatmap(im, valfmt="{x:.1f}")

    fig.tight_layout()
    plt.subplots_adjust(left=-0.05, bottom=0.15, right=0.99, top=0.95,
        wspace=0.0, hspace=0.0)
    plt.savefig("au_profile.pdf");

cmap_name="Reds"
def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw={}, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Arguments:
        data       : A 2D numpy array of shape (N,M)
        row_labels : A list or array of length N with the labels
                     for the rows
        col_labels : A list or array of length M with the labels
                     for the columns
    Optional arguments:
        ax         : A matplotlib.axes.Axes instance to which the heatmap
                     is plotted. If not provided, use current axes or
                     create a new one.
        cbar_kw    : A dictionary with arguments to
                     :meth:`matplotlib.Figure.colorbar`.
        cbarlabel  : The label for the colorbar
    All other arguments are directly passed on to the imshow call.
    """

    if not ax:
        ax = plt.gca()

    plt.rc('font', size=26)
    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # We want to show all ticks...
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_yticks(np.arange(data.shape[0]))
    # ... and label them with the respective list entries.
    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=False, bottom=True,
                   labeltop=False, labelbottom=True)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=0, ha="right",
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    for edge, spine in ax.spines.items():
        spine.set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)


    # # Loop over data dimensions and create text annotations.
    # for i in range(len(data)):
    #     for j in range(len(data[0])):
    #         text = ax.text(j, i, data[i, j],
    #                        ha="center", va="center", color="k")

    return im, cbar



def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=["black", "white"],
                     threshold=None, **textkw):
    """
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A list or array of two color specifications.  The first is used for
        values below a threshold, the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts


PlotAcc()
ProfileSoftwareSpeedupEnergy()
OpsReduction()
PlotLayerOps()
PlotPointNet()
PlotTimeDist()
ProfileHardwareEnergy()
ProfileHardwareSpeedup()
SystolicArraySpeedUp()
GroupSpeedUp()
SystolicArrayProfile()
profile_au()
TotalOps()
ProfileNSESpeedup()

