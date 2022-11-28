import shortuuid

def uploaded_files(instance, filename):
    
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (shortuuid.uuid(), ext)
    
    return os.path.join("uploaded_files/%s" % (filename))
