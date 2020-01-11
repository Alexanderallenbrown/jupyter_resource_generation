# jupyter_resource_generation

This is a repo to test the functionality of "generate_resource.py," a script that should be contained in the root of a "source" directory for a course that uses Jupyterhub and nbgrader.

The script is designed to allow you to compile a "summary resource" of all of the content on particular contents from your whole course.

When constructing your course assignment notebooks, use the "View->Cell Toolbars->Edit Metadata" toolbar to add metadata to cells to tell the script what course topic the cell is about.

For example, if I were teaching a Physics course, I might have topics like:

* Free Body Diagrams
* Newton's Laws
* Work and Energy

So if I was writing a cell that I'd later want to compile into a reference about "Newton's Laws" I would add this metadata to each relevant cell:

```
{
resourcetopic: "Newton's Laws"
}
```

To use the resource generation python script, modify the following lines in generate_resource.py to suit your course needs:

```python 
rootDir = './'
resourceDir = './Resource'
#create an empy notebook that will be our resource page
resnb = nbf.v4.new_notebook()
#create a filename. Won't use this until we actually write the notebook to file.
resource_fname = "Resource.ipynb"

#set the list of resource topic tags you want in your resource notebook. This
# can actually be strings or numbers, or mixed.
topic_list = [1,2]
```

In the example I just mentioned, you might change topic_list to:

```python
topic_list = ["Free Body Diagrams","Newton's Laws","Work and Energy"]
```

Then, run the file from the rootDir using python 3:

```bash 
$ python3 generate_resource.py
```
The script will crawl your source directory, which should be organized 

a test jupyter class where a script auto-generates a resource notebook.
