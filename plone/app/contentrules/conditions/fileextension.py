from persistent import Persistent 
from OFS.SimpleItem import SimpleItem

from zope.interface import implements, Interface
from zope.component import adapts
from zope.formlib import form
from zope import schema

from plone.contentrules.rule.interfaces import IExecutable, IRuleConditionData
from plone.contentrules.rule.rule import Node

from plone.app.contentrules.browser.formhelper import AddForm, EditForm 

class IFileExtensionCondition(IRuleConditionData):
    """Interface for the configurable aspects of a portal type condition.
    
    This is also used to create add and edit forms, below.
    """
    
    file_extension = schema.TextLine(title=u"File extension",
                                  description=u"The file extension to check for",
                                  required=True)
         
class FileExtensionCondition(SimpleItem):
    """The actual persistent implementation of the logger action element.
    
    Note that we must mix in Explicit to keep Zope 2 security happy.
    """
    implements(IFileExtensionCondition)
    
    file_extension = u''

class FileExtensionConditionExecutor(object):
    """The executor for this condition.
    
    This is registered as an adapter in configure.zcml
    """
    implements(IExecutable)
    adapts(Interface, IFileExtensionCondition, Interface)
         
    def __init__(self, context, element, event):
        self.context = context
        self.element = element
        self.event = event

    def __call__(self):
        kind = getattr(self.event.object, 'getPortalTypeName', None)()

        # Only act on files; folders etc have no "filename"
        if kind != 'File':
            return False
        
        name = getattr(self.event.object, 'getFilename', None)()
        extension = name[name.rfind('.')+1:]
        
        if extension == self.element.file_extension:
            import pdb; pdb.set_trace()
            
            return True
        
        return False
        
class FileExtensionAddForm(AddForm):
    """An add form for file extension rule conditions.
    
    Note that we create a Node(), not just a LoggerAction, since this is what
    the elements list of IRule expects. The namespace traversal adapter
    (see traversal.py) takes care of unwrapping the actual instance from
    a Node when it's needed.
    """
    form_fields = form.FormFields(IFileExtensionCondition)
    
    def create(self, data):
        c = FileExtensionCondition()
        c.file_extension = data.get('file_extension')
        return Node('plone.conditions.FileExtension', c)

class FileExtensionEditForm(EditForm):
    """An edit form for portal type conditions
    
    Formlib does all the magic here.
    """
    form_fields = form.FormFields(IFileExtensionCondition)