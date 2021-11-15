import matplotlib.pyplot as plt

x = 1

# Text Variables

class Block:

  def __init__(self, str_txt):
    self.txt = str_txt
    self.posx = 0.0
    self.posy = 0.0
    self.weight = 'regular'
    self.color = '#000000'
    self.size = 10
    self.alpha = 1
    self.prev = None
    self.dist = 0.02
    self.xshift = 0.0
    self.yshift = 0.0


  def __annotate__(self):
    plt.annotate(self.txt, (self.posx,self.posy), weight= self.weight, fontsize=self.size, alpha = self.alpha, color = self.color)

class Header(Block):

  def __init__(self, txt_str, mltply = 1):
    Block.__init__(self, txt_str)
    self.weight = 'bold'
    self.color = '#000000'
    self.size = 10*mltply
    self.alpha = 1
    self.dist = 0.025

class Top_Header(Block):

  def __init__(self, txt_str, mltply = 1):
    Block.__init__(self, txt_str)
    self.weight = 'bold'
    self.color = '#000000'
    self.size = 10*mltply
    self.alpha = 0.5
    self.dist = 0.035

class Name(Block):

  def __init__(self, txt_str, mltply = 1):
    Block.__init__(self, txt_str)
    self.weight = 'bold'
    self.color = '#000000'
    self.size = 20*mltply
    self.alpha = 1
    self.dist = 0.017

class Info(Block):

  def __init__(self, txt_str, mltply = 1):
    Block.__init__(self, txt_str)
    self.weight = 'regular'
    self.color = '#000000'
    self.size = 20*mltply
    self.alpha = 1

class Lateral(Block):

  def __init__(self, txt_str, mltply = 1):
    Block.__init__(self, txt_str)
    self.weight = 'regular'
    self.size = 9*mltply
    self.alpha = 1
    self.color = '#ffffff'

class Lateral_header(Block):

  def __init__(self, txt_str, mltply = 1):
    Block.__init__(self, txt_str)
    self.weight = 'bold'
    self.size = 12*mltply
    self.alpha = 1
    self.color = '#ffffff'
    self.dist = 0.025

class Lateral_title(Block):

  def __init__(self, txt_str, mltply = 1):
    Block.__init__(self, txt_str)
    self.weight = 'bold'
    self.size = 11*mltply
    self.alpha = 1
    self.color = '#ffffff'
    self.dist = 0.025    

class Title(Block):

  def __init__(self, txt_str, mltply = 1):
    Block.__init__(self, txt_str)
    self.weight = 'bold'
    self.size = 10*mltply
    self.alpha = 1
    self.dist = 0.025
    self.yshift = 0.005

class Place(Block):

  def __init__(self, txt_str, mltply = 1):
    Block.__init__(self, txt_str)
    self.weight = 'bold'
    self.size = 9.5*mltply
    self.alpha = 1
    self.dist = 0.025

class Descr(Block):

  def __init__(self, txt_str, mltply = 1):
    Block.__init__(self, txt_str)
    self.size = 9*mltply
    self.alpha = 1
    self.dist = 0.025

class Time(Block):

  def __init__(self, txt_str, mltply = 1):
    Block.__init__(self, txt_str)
    self.xshift = .55
    self.yshift = -.025
    self.size = 9*mltply
    self.alpha = 0.6
    self.dist = 0.025

class Train:

  def __init__(self,*args):
    self.blocks = [arg for arg in args]
    for i in range(1,len(self.blocks)):
      self.blocks[i].prev = self.blocks[i-1]
    
class Paragraph:
  
  def __init__(self, tuple_pos, train):
    train.blocks[0].posx = tuple_pos[0]
    train.blocks[0].posy = tuple_pos[1]
    train.blocks[0].__annotate__()
    self.head = train.blocks[0]
    for i in range(1,len(train.blocks)):
      train.blocks[i].prev = train.blocks[i-1]
      train.blocks[i].posx = self.head.posx + train.blocks[i].xshift
      train.blocks[i].posy = train.blocks[i].prev.posy - train.blocks[i].prev.dist - train.blocks[i].yshift
      train.blocks[i].__annotate__() 
    self.tail = train.blocks[-1]

#set colors
body_color = '#000000'
headers_color = '#58C1B2'

#set font
plt.rcParams['font.family'] = 'Sans-serif'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'

# Text Variables
#infos
Header1 = Top_Header('  Resume generated in Python - Full sourcecode in my portfolio',mltply = x)
Name1 = Name('STEFANO GALDO',mltply = x)
Pers1 = Descr('Birth: 27/11/1982 Tione di Trento, Italy',mltply = x)
Title1 = Title('Project Engineer - Lean Six Sigma Black Belt\nData Science & Analytics',mltply = x)
Contact1 = Lateral_title('Krakow, PL\n\n+39-3894358980\nstefanogaldo@gmail.com\n\nMy LinkedIn:\nlinkedin.com/in/stefano-galdo\n\nMy Github:\ngithub.com/Kaeltherol',mltply = x)

#projects

ProjectsHeader = Header('PROJECTS', mltply = x)

ProjectOneTitle = Title('Improvement of glass vials quality in Pharmaceutical industry', mltply = x)
ProjectOneDescL1 = Descr('- Analyzed product data to identify the source of defects', mltply = x)
ProjectOneDescL2 = Descr('- Cleaned/visualized quality data using pandas/matplotlib libraries in Python', mltply = x)

ProjectTwoTitle = Title('Scoring Supplier OTD (On Time Delivery) in Manufacturing Industry', mltply = x)
ProjectTwoDescL1 = Descr('- Assessing suppliers and purchase department performance', mltply = x)
ProjectTwoDescL2 = Descr('- Cleaned/visualized purchase data using pandas/matplotlib libraries in Python', mltply = x)


ProjectThreeTitle = Title('Increasing Reach and Impressions of a consultant company website', mltply = x)
ProjectThreeDesc = Descr('- Analyzed Google Analytics Data with pandas/matplotlib libraries in Python', mltply = x)

Portfolio = 'Portfolio website'

#work experience

WorkHeader = Header('EXPERIENCE',mltply = x)

WorkOneTitle = Title('Ravago Italy, Project Engineer',mltply = x)
WorkOnePlace = Place('Bergamo, Italy',mltply = x)

WorkOneTime = Time('2018-2020',mltply = x)
WorkOneDescL1 = Descr('- Project Management on Strategic Projects;',mltply = x)
WorkOneDescL2 = Descr('- Creation of a database in SQL for the implementation',mltply = x)
WorkOneDescL3 = Descr('  of a CMM Software (ULTIMO);',mltply = x)
WorkOneDescL4 = Descr('- Technical advice on Capex/Opex',mltply = x)

WorkTwoTitle = Title('Proplast / Materials Processing Lab Manager',mltply = x)
WorkTwoPlace = Place('Rivalta Scrivia, Italy',mltply = x)
WorkTwoTime = Time('2015-2018',mltply = x)
WorkTwoDescL1 = Descr('- Management of the polymers processing activities;',mltply = x)
WorkTwoDescL2 = Descr('- Customized technical assistance for compounding, extrusion',mltply = x)
WorkTwoDescL3 = Descr('  in different fields of application.',mltply = x)


WorkThreeTitle = Title('Ferrero SPA / R&D Engineer',mltply = x)
WorkThreePlace = Place('Alba, Italy',mltply = x)
WorkThreeTime = Time('2011-2013',mltply = x)
WorkThreeDesc = Descr('- Scaling up of pilot plant for snack packaging',mltply = x)

#education

EduHeader = Header('EDUCATION',mltply = x)
EduOneTitle = Title('Master\'s degree in Chemical Engineering',mltply = x) 
EduOnePlace = Place('Politecnico di Torino, Italy',mltply = x)
EduOneTime = Time('2015',mltply = x)
EduOneDesc1L1 = Descr('- Project Management, Algorithms for Plant Design',mltply = x)
EduOneDesc1L2 = Descr('  Basic Programming skills (C++, Python, Matlab) ',mltply = x)
EduTwoTitle = Title('Lean Six Sigma Black Belt, CROSSNOVA',mltply = x)
EduTwoTime = Time('2020',mltply = x)
EduOneDesc2L1 = Descr('- Brainstorming, statistics, FMEA, C&E diagram,',mltply = x)
EduOneDesc2L2 = Descr('  control plans, DOE, Measurement System Analysis',mltply = x)

#skills

SkillsHeader = Lateral_header('Computer Skills',mltply=x)
#SkillsDesc = Lateral('Skills\n- Python\n- Pandas\n- NumPy\n- Data Visualization\n- Data Cleaning\n- Command Line\n- Git and Version Control\n- SQL\n- APIs\n- Probability/Statistics\n- Data Manipulation\n- Excel',mltply =1)
SkillsTitle1 = Lateral_title('Python Skills',mltply =x)
SkillsDesc1L1 = Lateral('- Data Manipulation/Visualization:',mltply =x)
SkillsDesc1L2 = Lateral('   Numpy, Pandas, Matplotlib, Seaborn',mltply =x)
SkillsDesc1L3 = Lateral('   Scipy.',mltply =x)
SkillsDesc1L4 = Lateral('- Web Scraping:',mltply =x)
SkillsDesc1L5 = Lateral('   Selenium, Beautiful Soup.',mltply =x)
SkillsDesc1L6 = Lateral('- Testing:',mltply =x)
SkillsDesc1L7 = Lateral('   Unittest, Pytest, Silk',mltply =x)
SkillsDesc1L8 = Lateral('- Version Control:',mltply =x)
SkillsDesc1L9 = Lateral('   Git',mltply =x)
SkillsDesc1L10 = Lateral('- Data Structures, Algorithms',mltply =x)
SkillsTitle2 = Lateral_title('Other Skills', mltply=x)
SkillsDesc2L1 = Lateral('- Database Design and Management:',mltply=x)
SkillsDesc2L2 = Lateral('   SQL, MySQL, noSQL',mltply=x)
SkillsDesc2L3 = Lateral('- Probability and Statistics',mltply=x)
SkillsDesc2L4 = Lateral('- Troubleshooting',mltply=x)
SkillsTitle3 = Lateral_title('Soft Skills',mltply=x)
SkillsDesc3L1 = Lateral('- Communication',mltply=x)
SkillsDesc3L2 = Lateral('- Team work',mltply=x)
SkillsDesc3L3 = Lateral('- Time Management',mltply=x)
SkillsDesc3L4 = Lateral('- Negotiation',mltply=x)
ExtrasTitle = Lateral('DataQuest\nData Scientist Path', mltply=x)

CodeTitle = Lateral_title('View Portfolio', mltply=x)

train_info = Train(Header1, Name1, Pers1)
train_title = Train(Title1)
train_projects = Train(ProjectsHeader, ProjectOneTitle, ProjectOneDescL1, ProjectOneDescL2, ProjectTwoTitle, ProjectTwoDescL1, ProjectTwoDescL2, ProjectThreeTitle, ProjectThreeDesc)
train_work = Train(WorkHeader, WorkOneTitle, WorkOneTime, WorkOnePlace, WorkOneDescL1, WorkOneDescL2, WorkOneDescL3, WorkOneDescL4,
                            WorkTwoTitle, WorkTwoTime, WorkTwoPlace, WorkTwoDescL1, WorkTwoDescL2, WorkTwoDescL3,
                            WorkThreeTitle, WorkThreeTime, WorkThreePlace, WorkThreeDesc)
train_education = Train(EduHeader,EduOneTitle,EduOneTime,EduOnePlace,EduOneDesc1L1,EduOneDesc1L2,EduTwoTitle,EduTwoTime,EduOneDesc2L1,EduOneDesc2L2)

train_contacts = Train(Contact1)

train_lateral_header = Train(SkillsHeader)

train_lateral_1 = Train(SkillsTitle1,
                     SkillsDesc1L1, SkillsDesc1L2, SkillsDesc1L3, SkillsDesc1L4, 
                     SkillsDesc1L5, SkillsDesc1L6, SkillsDesc1L7, SkillsDesc1L8,
                     SkillsDesc1L9, SkillsDesc1L10)

train_lateral_2 = Train(SkillsTitle2,
                     SkillsDesc2L1, SkillsDesc2L2, SkillsDesc2L3, SkillsDesc2L4)
train_lateral_3 = Train(SkillsTitle3,
                     SkillsDesc3L1, SkillsDesc3L2, SkillsDesc3L3, SkillsDesc3L4)

train_code = Train(CodeTitle)

#setting plot
fig, ax = plt.subplots(figsize=(8.5*x, 11*x))
#ax2 = ax.twiny()
#remove axis
plt.axis('off')

plt.axvline(x=.99, color='#000000', alpha=0.5, linewidth=300*x)
plt.axhline(y=.8, xmin=0, xmax=1, color='#ffffff', linewidth=3)

personal_data = Paragraph((.02,.98), train_info)
title = Paragraph((0.02, 0.885), train_title)
projects = Paragraph((.02, 0.855), train_projects)
work = Paragraph((0.02, 0.605),train_work)
edu = Paragraph((0.02, 0.2),train_education)
contact = Paragraph((0.68,0.81),train_contacts)
skills_0 =Paragraph((0.68,0.775),train_lateral_header)
skills_1 = Paragraph((0.68,0.735),train_lateral_1)
skills_2 = Paragraph((0.68,0.49),train_lateral_2)
skills_3 = Paragraph((0.68,0.370),train_lateral_3)
code = Paragraph((0.68,0.235), train_code)

from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.image as mpimg
arr_code = mpimg.imread(r'C:\Users\mmari\Pictures\Stefanogaldo.png')
imagebox = OffsetImage(arr_code, zoom=0.5)
ab = AnnotationBbox(imagebox, (0.84, 0.12))
ax.add_artist(ab)

plt.savefig('resumeexample.png', dpi=300, bbox_inches='tight')

plt.show()