# Import the os module, for the os.walk function
import os

import nbformat as nbf 

# Set the directory you want to start from
rootDir = './'
resourceDir = './Resource'
#create an empy notebook that will be our resource page
resnb = nbf.v4.new_notebook()
#create a filename. Won't use this until we actually write the notebook to file.
resource_fname = resourceDir+"/"+"Resource.ipynb"

if not os.path.exists(resourceDir):
    os.mkdir(resourceDir)
    
if os.path.exists(resource_fname):
    os.remove(resource_fname)

#variable to determine whether you want context links:
addContextLinks = True

#a variable to hold our cells, one by one.
cells = []

#set the list of resource topic tags you want in your resource notebook. This
# can actually be strings or numbers, or mixed.
topic_list = [1,2]

#whitelist a set of directories
dir_list = ['Reading_1','Reading_2']
for topic in topic_list:
    #create a main heading for this topic
    this_cell = nbf.v4.new_markdown_cell(source="# "+str(topic)) #this should be a main, level-1 heading.
    cells.append(this_cell)
    #add this cell to our notebook.

    #now we will try to find any content in our source directory that falls under this topic, and stick it in.
    for dirName, subdirList, fileList in os.walk(rootDir):
        
        if len(dirName)>len(rootDir) and dirName[len(rootDir)] is not "." and dirName is not resourceDir:
            print('Found directory: %s' % dirName)
            if (not ("checkpoint" in dirName)) and (dirName[len(rootDir):] in dir_list):
                for fname in fileList:
                    if fname[0] is not '.' and fname is not resource_fname:
                        #if this is a jupyter notebook
                        if fname[-6:]==".ipynb":
                            #make sure it is not a checkpoint file.
                            if not resource_fname in fname:
                                #which notebook?
                                print('\t%s' % fname)
                                #read the notebook
                                ntbk = nbf.read(dirName+"/"+fname, nbf.NO_CONVERT) 

                                for cell in ntbk.cells:
                                    if hasattr(cell.metadata, 'resourcetopic'):
                                        #print(cell.metadata.resourcetopic)
                                        #check if this is the topic we want.
                                        if cell.metadata.resourcetopic == topic:
                                            cells.append(cell)
                                            #If a markdown cell with a heading has metadata then create context link
                                            sourceString = cell.source
                                            if (sourceString[0] == '#' and cell.cell_type == 'markdown' and addContextLinks):
                                                #strip hashtags and leading space from markdown formatting
                                                linkString = sourceString[sourceString.find(' ')+1:].splitlines()[0]
                                                linkString = '#'+linkString.replace(' ','-')
                                                #build link path using filename (without suffix) and in page link
                                                sourcePath = "<a href=\" " +"."+ dirName+ "/" + fname+ linkString +" \" > Link to Original Context in: " + fname[0:fname.find('.')] +"</a>"
                                                contextcell = nbf.v4.new_markdown_cell(source=sourcePath) 
                                                # replace all heading cues with second-level headings.
                                                sourceString = '## '+sourceString.replace('#','')
                                                cells.append(contextcell)  
                                    else:
                                        pass
                                        #print("this cell is not a resource cell")


#add our cells to the notebook object
resnb['cells'].extend(cells)

#write the resource notebook to a file
nbf.write(resnb,resource_fname)
