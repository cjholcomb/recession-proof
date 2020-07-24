from lookups import *
from helper_functions import *
from list_maker import *

class Industry(object):
    #Collects all the important info about an industry

def __init__(self, code):
    self.code = code
    self.title = all_industries [code]
    if code < 100:
        self.generation = 1
    elif code < 1000:
        self.generation = 2
    elif code < 10000:
        self.generation = 3
    elif code < 100000:
        self.generation = 4
    elif code < 1000000:
        self.generation = 5
    if self.code = 10:
        self.parent = None
    elif self.generation = 1:
        self.parent = 10
    elif code in weird_indus
        self.parent = code // 10
    else:
        parent = code //10
        parentgen = self.generation - 1
        while parent not in generation_dict[parentgen]:
            parent = -1
        self.parent = parent  
    self.cohort = generation_dict[self.generation].remove(code)
    # self.siblings = []
    # self.cousins = []
    # self.children = []

def timeline_alone(self, df, code):
    fig, ax = plt.subplots()
    x = df.columns.values[2:]
    y = df[df['industry_code'] == code].values[0][2:]
    label = df[df['industry_code'] == code].values[0][1]
    ax.plot(x,y,label = label)
    ax.legend(bbox_to_anchor = (1,1), fancybox = True)
    plt.show();

def timeline_wparent(self,df, code):
    fig, ax = plt.subplots()
    x = df.columns.values[2:]
    y = df[df['industry_code'] == code].values[0][2:]
    label = df[df['industry_code'] == code].values[0][1]
    ax.plot(x,y,label = label)
    y = df[df['industry_code'] == self.parent].values[0][2:]
    label = df[df['industry_code'] == self.parent].values[0][1]
    ax.plot(x,y,label = label)
    ax.legend(bbox_to_anchor = (1,1), fancybox = True)
    plt.show();

def timeline_wchildren(self, df, code):
    pass

def timeline_wsiblings(self, df, code):
    pass

def compute_peak(self, df, code):
    df_firm = df.pivot_table(columns = 'qtrid', values = 'qtrly_estabs_count', index = ['industry_code', 'industry_title'], aggfunc = np.max)
    df_firm = df_firm.reset_index()
    df_empl = df.pivot_table(columns = 'qtrid', values = 'qtrly_estabs_count', index = ['industry_code', 'industry_title'], aggfunc = np.max)
    df_empl = df_empl.reset_index()
    df_wage = df.pivot_table(columns = 'qtrid', values = 'avg_wkly_wage', index = ['industry_code', 'industry_title'], aggfunc = np.min)
    df_wage = df_wage.reset_index()
    self.emplPeak = max(df_empl[df_empl['industry_code'] == industry_code].values[0][2:10])
    self.firmPeak = max(df_firm[df_empl['industry_code'] == industry_code].values[0][2:10])
    self.wagePeak = max(df_wage[df_empl['industry_code'] == industry_code].values[0][2:10])

def compute_growth(self, df, code):
    df_firm = df.pivot_table(columns = 'qtrid', values = 'qtrly_estabs_count', index = ['industry_code', 'industry_title'], aggfunc = np.max)
    df_firm = df_firm.reset_index()
    df_empl = df.pivot_table(columns = 'qtrid', values = 'qtrly_estabs_count', index = ['industry_code', 'industry_title'], aggfunc = np.max)
    df_empl = df_empl.reset_index()
    df_wage = df.pivot_table(columns = 'qtrid', values = 'avg_wkly_wage', index = ['industry_code', 'industry_title'], aggfunc = np.min)
    df_wage = df_wage.reset_index()
    self.emplPeak = max(df_empl[df_empl['industry_code'] == industry_code].values[0][2:10])
    self.firmPeak = max(df_firm[df_empl['industry_code'] == industry_code].values[0][2:10])
    self.wagePeak = max(df_wage[df_empl['industry_code'] == industry_code].values[0][2:10])
    self.emplGrowth = df_empl.iloc[0,33] - self.emplPeak
    self.firmGrowth = df_firm.iloc[0,33] - self.firmPeak
    self.wageGrowth = df_wage.iloc[0,33] - self.wagePeak 

# def find_generation(self, code):
#     if code < 100:
#         self.generation = 1
#     elif code < 1000:
#         self.generation = 2
#     elif code < 10000:
#         self.generation = 3
#     elif code < 100000:
#         self.generation = 4
#     elif code < 1000000:
#         self.generation = 5

# def find_parent(self, code):
#     if self.code = 10:
#         self.parent = None
#     elif self.generation = 1:
#         self.parent = 10
#     elif code in weird_indus
#         self.parent = code // 10
#     else:
#         parent = code //10
#         parentgen = self.generation - 1
#         while parent not in generation_dict[parentgen]:
#             parent = -1
#         self.parent = parent

# def find_cousins(self,code):
#     self.cousins = generation_dict[self.generation].remove(code) 

# def find_siblings(self, code):
#     if self.generation = 0:
#         self.generation = find_generation
#     if self.parent = 0:
#         self.parent = find_parent(self, code)

    

