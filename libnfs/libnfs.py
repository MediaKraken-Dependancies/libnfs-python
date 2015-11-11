# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.5
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_libnfs', [dirname(__file__)])
        except ImportError:
            import _libnfs
            return _libnfs
        if fp is not None:
            try:
                _mod = imp.load_module('_libnfs', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _libnfs = swig_import_helper()
    del swig_import_helper
else:
    import _libnfs
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



def new_NFSFileHandle():
    return _libnfs.new_NFSFileHandle()
new_NFSFileHandle = _libnfs.new_NFSFileHandle

def copy_NFSFileHandle(value):
    return _libnfs.copy_NFSFileHandle(value)
copy_NFSFileHandle = _libnfs.copy_NFSFileHandle

def delete_NFSFileHandle(obj):
    return _libnfs.delete_NFSFileHandle(obj)
delete_NFSFileHandle = _libnfs.delete_NFSFileHandle

def NFSFileHandle_assign(obj, value):
    return _libnfs.NFSFileHandle_assign(obj, value)
NFSFileHandle_assign = _libnfs.NFSFileHandle_assign

def NFSFileHandle_value(obj):
    return _libnfs.NFSFileHandle_value(obj)
NFSFileHandle_value = _libnfs.NFSFileHandle_value

def new_uint64_t_ptr():
    return _libnfs.new_uint64_t_ptr()
new_uint64_t_ptr = _libnfs.new_uint64_t_ptr

def copy_uint64_t_ptr(value):
    return _libnfs.copy_uint64_t_ptr(value)
copy_uint64_t_ptr = _libnfs.copy_uint64_t_ptr

def delete_uint64_t_ptr(obj):
    return _libnfs.delete_uint64_t_ptr(obj)
delete_uint64_t_ptr = _libnfs.delete_uint64_t_ptr

def uint64_t_ptr_assign(obj, value):
    return _libnfs.uint64_t_ptr_assign(obj, value)
uint64_t_ptr_assign = _libnfs.uint64_t_ptr_assign

def uint64_t_ptr_value(obj):
    return _libnfs.uint64_t_ptr_value(obj)
uint64_t_ptr_value = _libnfs.uint64_t_ptr_value
class nfs_url(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, nfs_url, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, nfs_url, name)
    __repr__ = _swig_repr
    __swig_setmethods__["server"] = _libnfs.nfs_url_server_set
    __swig_getmethods__["server"] = _libnfs.nfs_url_server_get
    if _newclass:
        server = _swig_property(_libnfs.nfs_url_server_get, _libnfs.nfs_url_server_set)
    __swig_setmethods__["path"] = _libnfs.nfs_url_path_set
    __swig_getmethods__["path"] = _libnfs.nfs_url_path_get
    if _newclass:
        path = _swig_property(_libnfs.nfs_url_path_get, _libnfs.nfs_url_path_set)
    __swig_setmethods__["file"] = _libnfs.nfs_url_file_set
    __swig_getmethods__["file"] = _libnfs.nfs_url_file_get
    if _newclass:
        file = _swig_property(_libnfs.nfs_url_file_get, _libnfs.nfs_url_file_set)

    def __init__(self):
        this = _libnfs.new_nfs_url()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _libnfs.delete_nfs_url
    __del__ = lambda self: None
nfs_url_swigregister = _libnfs.nfs_url_swigregister
nfs_url_swigregister(nfs_url)

class nfs_stat_64(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, nfs_stat_64, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, nfs_stat_64, name)
    __repr__ = _swig_repr
    __swig_setmethods__["nfs_dev"] = _libnfs.nfs_stat_64_nfs_dev_set
    __swig_getmethods__["nfs_dev"] = _libnfs.nfs_stat_64_nfs_dev_get
    if _newclass:
        nfs_dev = _swig_property(_libnfs.nfs_stat_64_nfs_dev_get, _libnfs.nfs_stat_64_nfs_dev_set)
    __swig_setmethods__["nfs_ino"] = _libnfs.nfs_stat_64_nfs_ino_set
    __swig_getmethods__["nfs_ino"] = _libnfs.nfs_stat_64_nfs_ino_get
    if _newclass:
        nfs_ino = _swig_property(_libnfs.nfs_stat_64_nfs_ino_get, _libnfs.nfs_stat_64_nfs_ino_set)
    __swig_setmethods__["nfs_mode"] = _libnfs.nfs_stat_64_nfs_mode_set
    __swig_getmethods__["nfs_mode"] = _libnfs.nfs_stat_64_nfs_mode_get
    if _newclass:
        nfs_mode = _swig_property(_libnfs.nfs_stat_64_nfs_mode_get, _libnfs.nfs_stat_64_nfs_mode_set)
    __swig_setmethods__["nfs_nlink"] = _libnfs.nfs_stat_64_nfs_nlink_set
    __swig_getmethods__["nfs_nlink"] = _libnfs.nfs_stat_64_nfs_nlink_get
    if _newclass:
        nfs_nlink = _swig_property(_libnfs.nfs_stat_64_nfs_nlink_get, _libnfs.nfs_stat_64_nfs_nlink_set)
    __swig_setmethods__["nfs_uid"] = _libnfs.nfs_stat_64_nfs_uid_set
    __swig_getmethods__["nfs_uid"] = _libnfs.nfs_stat_64_nfs_uid_get
    if _newclass:
        nfs_uid = _swig_property(_libnfs.nfs_stat_64_nfs_uid_get, _libnfs.nfs_stat_64_nfs_uid_set)
    __swig_setmethods__["nfs_gid"] = _libnfs.nfs_stat_64_nfs_gid_set
    __swig_getmethods__["nfs_gid"] = _libnfs.nfs_stat_64_nfs_gid_get
    if _newclass:
        nfs_gid = _swig_property(_libnfs.nfs_stat_64_nfs_gid_get, _libnfs.nfs_stat_64_nfs_gid_set)
    __swig_setmethods__["nfs_rdev"] = _libnfs.nfs_stat_64_nfs_rdev_set
    __swig_getmethods__["nfs_rdev"] = _libnfs.nfs_stat_64_nfs_rdev_get
    if _newclass:
        nfs_rdev = _swig_property(_libnfs.nfs_stat_64_nfs_rdev_get, _libnfs.nfs_stat_64_nfs_rdev_set)
    __swig_setmethods__["nfs_size"] = _libnfs.nfs_stat_64_nfs_size_set
    __swig_getmethods__["nfs_size"] = _libnfs.nfs_stat_64_nfs_size_get
    if _newclass:
        nfs_size = _swig_property(_libnfs.nfs_stat_64_nfs_size_get, _libnfs.nfs_stat_64_nfs_size_set)
    __swig_setmethods__["nfs_blksize"] = _libnfs.nfs_stat_64_nfs_blksize_set
    __swig_getmethods__["nfs_blksize"] = _libnfs.nfs_stat_64_nfs_blksize_get
    if _newclass:
        nfs_blksize = _swig_property(_libnfs.nfs_stat_64_nfs_blksize_get, _libnfs.nfs_stat_64_nfs_blksize_set)
    __swig_setmethods__["nfs_blocks"] = _libnfs.nfs_stat_64_nfs_blocks_set
    __swig_getmethods__["nfs_blocks"] = _libnfs.nfs_stat_64_nfs_blocks_get
    if _newclass:
        nfs_blocks = _swig_property(_libnfs.nfs_stat_64_nfs_blocks_get, _libnfs.nfs_stat_64_nfs_blocks_set)
    __swig_setmethods__["nfs_atime"] = _libnfs.nfs_stat_64_nfs_atime_set
    __swig_getmethods__["nfs_atime"] = _libnfs.nfs_stat_64_nfs_atime_get
    if _newclass:
        nfs_atime = _swig_property(_libnfs.nfs_stat_64_nfs_atime_get, _libnfs.nfs_stat_64_nfs_atime_set)
    __swig_setmethods__["nfs_mtime"] = _libnfs.nfs_stat_64_nfs_mtime_set
    __swig_getmethods__["nfs_mtime"] = _libnfs.nfs_stat_64_nfs_mtime_get
    if _newclass:
        nfs_mtime = _swig_property(_libnfs.nfs_stat_64_nfs_mtime_get, _libnfs.nfs_stat_64_nfs_mtime_set)
    __swig_setmethods__["nfs_ctime"] = _libnfs.nfs_stat_64_nfs_ctime_set
    __swig_getmethods__["nfs_ctime"] = _libnfs.nfs_stat_64_nfs_ctime_get
    if _newclass:
        nfs_ctime = _swig_property(_libnfs.nfs_stat_64_nfs_ctime_get, _libnfs.nfs_stat_64_nfs_ctime_set)
    __swig_setmethods__["nfs_atime_nsec"] = _libnfs.nfs_stat_64_nfs_atime_nsec_set
    __swig_getmethods__["nfs_atime_nsec"] = _libnfs.nfs_stat_64_nfs_atime_nsec_get
    if _newclass:
        nfs_atime_nsec = _swig_property(_libnfs.nfs_stat_64_nfs_atime_nsec_get, _libnfs.nfs_stat_64_nfs_atime_nsec_set)
    __swig_setmethods__["nfs_mtime_nsec"] = _libnfs.nfs_stat_64_nfs_mtime_nsec_set
    __swig_getmethods__["nfs_mtime_nsec"] = _libnfs.nfs_stat_64_nfs_mtime_nsec_get
    if _newclass:
        nfs_mtime_nsec = _swig_property(_libnfs.nfs_stat_64_nfs_mtime_nsec_get, _libnfs.nfs_stat_64_nfs_mtime_nsec_set)
    __swig_setmethods__["nfs_ctime_nsec"] = _libnfs.nfs_stat_64_nfs_ctime_nsec_set
    __swig_getmethods__["nfs_ctime_nsec"] = _libnfs.nfs_stat_64_nfs_ctime_nsec_get
    if _newclass:
        nfs_ctime_nsec = _swig_property(_libnfs.nfs_stat_64_nfs_ctime_nsec_get, _libnfs.nfs_stat_64_nfs_ctime_nsec_set)
    __swig_setmethods__["nfs_used"] = _libnfs.nfs_stat_64_nfs_used_set
    __swig_getmethods__["nfs_used"] = _libnfs.nfs_stat_64_nfs_used_get
    if _newclass:
        nfs_used = _swig_property(_libnfs.nfs_stat_64_nfs_used_get, _libnfs.nfs_stat_64_nfs_used_set)

    def __init__(self):
        this = _libnfs.new_nfs_stat_64()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _libnfs.delete_nfs_stat_64
    __del__ = lambda self: None
nfs_stat_64_swigregister = _libnfs.nfs_stat_64_swigregister
nfs_stat_64_swigregister(nfs_stat_64)

class nfsdirent(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, nfsdirent, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, nfsdirent, name)
    __repr__ = _swig_repr
    __swig_setmethods__["next"] = _libnfs.nfsdirent_next_set
    __swig_getmethods__["next"] = _libnfs.nfsdirent_next_get
    if _newclass:
        next = _swig_property(_libnfs.nfsdirent_next_get, _libnfs.nfsdirent_next_set)
    __swig_setmethods__["name"] = _libnfs.nfsdirent_name_set
    __swig_getmethods__["name"] = _libnfs.nfsdirent_name_get
    if _newclass:
        name = _swig_property(_libnfs.nfsdirent_name_get, _libnfs.nfsdirent_name_set)
    __swig_setmethods__["inode"] = _libnfs.nfsdirent_inode_set
    __swig_getmethods__["inode"] = _libnfs.nfsdirent_inode_get
    if _newclass:
        inode = _swig_property(_libnfs.nfsdirent_inode_get, _libnfs.nfsdirent_inode_set)
    __swig_setmethods__["type"] = _libnfs.nfsdirent_type_set
    __swig_getmethods__["type"] = _libnfs.nfsdirent_type_get
    if _newclass:
        type = _swig_property(_libnfs.nfsdirent_type_get, _libnfs.nfsdirent_type_set)
    __swig_setmethods__["mode"] = _libnfs.nfsdirent_mode_set
    __swig_getmethods__["mode"] = _libnfs.nfsdirent_mode_get
    if _newclass:
        mode = _swig_property(_libnfs.nfsdirent_mode_get, _libnfs.nfsdirent_mode_set)
    __swig_setmethods__["size"] = _libnfs.nfsdirent_size_set
    __swig_getmethods__["size"] = _libnfs.nfsdirent_size_get
    if _newclass:
        size = _swig_property(_libnfs.nfsdirent_size_get, _libnfs.nfsdirent_size_set)
    __swig_setmethods__["atime"] = _libnfs.nfsdirent_atime_set
    __swig_getmethods__["atime"] = _libnfs.nfsdirent_atime_get
    if _newclass:
        atime = _swig_property(_libnfs.nfsdirent_atime_get, _libnfs.nfsdirent_atime_set)
    __swig_setmethods__["mtime"] = _libnfs.nfsdirent_mtime_set
    __swig_getmethods__["mtime"] = _libnfs.nfsdirent_mtime_get
    if _newclass:
        mtime = _swig_property(_libnfs.nfsdirent_mtime_get, _libnfs.nfsdirent_mtime_set)
    __swig_setmethods__["ctime"] = _libnfs.nfsdirent_ctime_set
    __swig_getmethods__["ctime"] = _libnfs.nfsdirent_ctime_get
    if _newclass:
        ctime = _swig_property(_libnfs.nfsdirent_ctime_get, _libnfs.nfsdirent_ctime_set)
    __swig_setmethods__["uid"] = _libnfs.nfsdirent_uid_set
    __swig_getmethods__["uid"] = _libnfs.nfsdirent_uid_get
    if _newclass:
        uid = _swig_property(_libnfs.nfsdirent_uid_get, _libnfs.nfsdirent_uid_set)
    __swig_setmethods__["gid"] = _libnfs.nfsdirent_gid_set
    __swig_getmethods__["gid"] = _libnfs.nfsdirent_gid_get
    if _newclass:
        gid = _swig_property(_libnfs.nfsdirent_gid_get, _libnfs.nfsdirent_gid_set)
    __swig_setmethods__["nlink"] = _libnfs.nfsdirent_nlink_set
    __swig_getmethods__["nlink"] = _libnfs.nfsdirent_nlink_get
    if _newclass:
        nlink = _swig_property(_libnfs.nfsdirent_nlink_get, _libnfs.nfsdirent_nlink_set)
    __swig_setmethods__["dev"] = _libnfs.nfsdirent_dev_set
    __swig_getmethods__["dev"] = _libnfs.nfsdirent_dev_get
    if _newclass:
        dev = _swig_property(_libnfs.nfsdirent_dev_get, _libnfs.nfsdirent_dev_set)
    __swig_setmethods__["rdev"] = _libnfs.nfsdirent_rdev_set
    __swig_getmethods__["rdev"] = _libnfs.nfsdirent_rdev_get
    if _newclass:
        rdev = _swig_property(_libnfs.nfsdirent_rdev_get, _libnfs.nfsdirent_rdev_set)
    __swig_setmethods__["blksize"] = _libnfs.nfsdirent_blksize_set
    __swig_getmethods__["blksize"] = _libnfs.nfsdirent_blksize_get
    if _newclass:
        blksize = _swig_property(_libnfs.nfsdirent_blksize_get, _libnfs.nfsdirent_blksize_set)
    __swig_setmethods__["blocks"] = _libnfs.nfsdirent_blocks_set
    __swig_getmethods__["blocks"] = _libnfs.nfsdirent_blocks_get
    if _newclass:
        blocks = _swig_property(_libnfs.nfsdirent_blocks_get, _libnfs.nfsdirent_blocks_set)
    __swig_setmethods__["used"] = _libnfs.nfsdirent_used_set
    __swig_getmethods__["used"] = _libnfs.nfsdirent_used_get
    if _newclass:
        used = _swig_property(_libnfs.nfsdirent_used_get, _libnfs.nfsdirent_used_set)
    __swig_setmethods__["atime_nsec"] = _libnfs.nfsdirent_atime_nsec_set
    __swig_getmethods__["atime_nsec"] = _libnfs.nfsdirent_atime_nsec_get
    if _newclass:
        atime_nsec = _swig_property(_libnfs.nfsdirent_atime_nsec_get, _libnfs.nfsdirent_atime_nsec_set)
    __swig_setmethods__["mtime_nsec"] = _libnfs.nfsdirent_mtime_nsec_set
    __swig_getmethods__["mtime_nsec"] = _libnfs.nfsdirent_mtime_nsec_get
    if _newclass:
        mtime_nsec = _swig_property(_libnfs.nfsdirent_mtime_nsec_get, _libnfs.nfsdirent_mtime_nsec_set)
    __swig_setmethods__["ctime_nsec"] = _libnfs.nfsdirent_ctime_nsec_set
    __swig_getmethods__["ctime_nsec"] = _libnfs.nfsdirent_ctime_nsec_get
    if _newclass:
        ctime_nsec = _swig_property(_libnfs.nfsdirent_ctime_nsec_get, _libnfs.nfsdirent_ctime_nsec_set)

    def __init__(self):
        this = _libnfs.new_nfsdirent()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _libnfs.delete_nfsdirent
    __del__ = lambda self: None
nfsdirent_swigregister = _libnfs.nfsdirent_swigregister
nfsdirent_swigregister(nfsdirent)

class nfs_server_list(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, nfs_server_list, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, nfs_server_list, name)
    __repr__ = _swig_repr
    __swig_setmethods__["next"] = _libnfs.nfs_server_list_next_set
    __swig_getmethods__["next"] = _libnfs.nfs_server_list_next_get
    if _newclass:
        next = _swig_property(_libnfs.nfs_server_list_next_get, _libnfs.nfs_server_list_next_set)
    __swig_setmethods__["addr"] = _libnfs.nfs_server_list_addr_set
    __swig_getmethods__["addr"] = _libnfs.nfs_server_list_addr_get
    if _newclass:
        addr = _swig_property(_libnfs.nfs_server_list_addr_get, _libnfs.nfs_server_list_addr_set)

    def __init__(self):
        this = _libnfs.new_nfs_server_list()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _libnfs.delete_nfs_server_list
    __del__ = lambda self: None
nfs_server_list_swigregister = _libnfs.nfs_server_list_swigregister
nfs_server_list_swigregister(nfs_server_list)


def nfs_init_context():
    return _libnfs.nfs_init_context()
nfs_init_context = _libnfs.nfs_init_context

def nfs_destroy_context(nfs):
    return _libnfs.nfs_destroy_context(nfs)
nfs_destroy_context = _libnfs.nfs_destroy_context

def nfs_get_error(nfs):
    return _libnfs.nfs_get_error(nfs)
nfs_get_error = _libnfs.nfs_get_error

def nfs_set_auth(nfs, auth):
    return _libnfs.nfs_set_auth(nfs, auth)
nfs_set_auth = _libnfs.nfs_set_auth

def nfs_parse_url_full(nfs, url):
    return _libnfs.nfs_parse_url_full(nfs, url)
nfs_parse_url_full = _libnfs.nfs_parse_url_full

def nfs_parse_url_dir(nfs, url):
    return _libnfs.nfs_parse_url_dir(nfs, url)
nfs_parse_url_dir = _libnfs.nfs_parse_url_dir

def nfs_parse_url_incomplete(nfs, url):
    return _libnfs.nfs_parse_url_incomplete(nfs, url)
nfs_parse_url_incomplete = _libnfs.nfs_parse_url_incomplete

def nfs_destroy_url(url):
    return _libnfs.nfs_destroy_url(url)
nfs_destroy_url = _libnfs.nfs_destroy_url

def nfs_get_readmax(nfs):
    return _libnfs.nfs_get_readmax(nfs)
nfs_get_readmax = _libnfs.nfs_get_readmax

def nfs_get_writemax(nfs):
    return _libnfs.nfs_get_writemax(nfs)
nfs_get_writemax = _libnfs.nfs_get_writemax

def nfs_set_tcp_syncnt(nfs, v):
    return _libnfs.nfs_set_tcp_syncnt(nfs, v)
nfs_set_tcp_syncnt = _libnfs.nfs_set_tcp_syncnt

def nfs_set_uid(nfs, uid):
    return _libnfs.nfs_set_uid(nfs, uid)
nfs_set_uid = _libnfs.nfs_set_uid

def nfs_set_gid(nfs, gid):
    return _libnfs.nfs_set_gid(nfs, gid)
nfs_set_gid = _libnfs.nfs_set_gid

def nfs_set_readahead(nfs, v):
    return _libnfs.nfs_set_readahead(nfs, v)
nfs_set_readahead = _libnfs.nfs_set_readahead

def nfs_mount(nfs, server, exportname):
    return _libnfs.nfs_mount(nfs, server, exportname)
nfs_mount = _libnfs.nfs_mount

def nfs_stat64(nfs, path, st):
    return _libnfs.nfs_stat64(nfs, path, st)
nfs_stat64 = _libnfs.nfs_stat64

def nfs_lstat64(nfs, path, st):
    return _libnfs.nfs_lstat64(nfs, path, st)
nfs_lstat64 = _libnfs.nfs_lstat64

def nfs_fstat64(nfs, nfsfh, st):
    return _libnfs.nfs_fstat64(nfs, nfsfh, st)
nfs_fstat64 = _libnfs.nfs_fstat64

def nfs_open(nfs, path, flags, nfsfh):
    return _libnfs.nfs_open(nfs, path, flags, nfsfh)
nfs_open = _libnfs.nfs_open

def nfs_close(nfs, nfsfh):
    return _libnfs.nfs_close(nfs, nfsfh)
nfs_close = _libnfs.nfs_close

def nfs_pread(nfs, nfsfh, offset, count, buff):
    return _libnfs.nfs_pread(nfs, nfsfh, offset, count, buff)
nfs_pread = _libnfs.nfs_pread

def nfs_read(nfs, nfsfh, count, buff):
    return _libnfs.nfs_read(nfs, nfsfh, count, buff)
nfs_read = _libnfs.nfs_read

def nfs_pwrite(nfs, nfsfh, offset, count, buff):
    return _libnfs.nfs_pwrite(nfs, nfsfh, offset, count, buff)
nfs_pwrite = _libnfs.nfs_pwrite

def nfs_write(nfs, nfsfh, count, buff):
    return _libnfs.nfs_write(nfs, nfsfh, count, buff)
nfs_write = _libnfs.nfs_write

def nfs_lseek(nfs, nfsfh, offset, whence, current_offset):
    return _libnfs.nfs_lseek(nfs, nfsfh, offset, whence, current_offset)
nfs_lseek = _libnfs.nfs_lseek

def nfs_fsync(nfs, nfsfh):
    return _libnfs.nfs_fsync(nfs, nfsfh)
nfs_fsync = _libnfs.nfs_fsync

def nfs_truncate(nfs, path, length):
    return _libnfs.nfs_truncate(nfs, path, length)
nfs_truncate = _libnfs.nfs_truncate

def nfs_ftruncate(nfs, nfsfh, length):
    return _libnfs.nfs_ftruncate(nfs, nfsfh, length)
nfs_ftruncate = _libnfs.nfs_ftruncate

def nfs_mkdir(nfs, path):
    return _libnfs.nfs_mkdir(nfs, path)
nfs_mkdir = _libnfs.nfs_mkdir

def nfs_rmdir(nfs, path):
    return _libnfs.nfs_rmdir(nfs, path)
nfs_rmdir = _libnfs.nfs_rmdir

def nfs_creat(nfs, path, mode, nfsfh):
    return _libnfs.nfs_creat(nfs, path, mode, nfsfh)
nfs_creat = _libnfs.nfs_creat

def nfs_create(nfs, path, flags, mode, nfsfh):
    return _libnfs.nfs_create(nfs, path, flags, mode, nfsfh)
nfs_create = _libnfs.nfs_create

def nfs_mknod(nfs, path, mode, dev):
    return _libnfs.nfs_mknod(nfs, path, mode, dev)
nfs_mknod = _libnfs.nfs_mknod

def nfs_unlink(nfs, path):
    return _libnfs.nfs_unlink(nfs, path)
nfs_unlink = _libnfs.nfs_unlink

def nfs_opendir(nfs, path, nfsdir):
    return _libnfs.nfs_opendir(nfs, path, nfsdir)
nfs_opendir = _libnfs.nfs_opendir

def nfs_readdir(nfs, nfsdir):
    return _libnfs.nfs_readdir(nfs, nfsdir)
nfs_readdir = _libnfs.nfs_readdir

def nfs_closedir(nfs, nfsdir):
    return _libnfs.nfs_closedir(nfs, nfsdir)
nfs_closedir = _libnfs.nfs_closedir

def nfs_chdir(nfs, path):
    return _libnfs.nfs_chdir(nfs, path)
nfs_chdir = _libnfs.nfs_chdir

def nfs_getcwd(nfs, cwd):
    return _libnfs.nfs_getcwd(nfs, cwd)
nfs_getcwd = _libnfs.nfs_getcwd

def nfs_readlink(nfs, path, buff, bufsize):
    return _libnfs.nfs_readlink(nfs, path, buff, bufsize)
nfs_readlink = _libnfs.nfs_readlink

def nfs_chmod(nfs, path, mode):
    return _libnfs.nfs_chmod(nfs, path, mode)
nfs_chmod = _libnfs.nfs_chmod

def nfs_lchmod(nfs, path, mode):
    return _libnfs.nfs_lchmod(nfs, path, mode)
nfs_lchmod = _libnfs.nfs_lchmod

def nfs_fchmod(nfs, nfsfh, mode):
    return _libnfs.nfs_fchmod(nfs, nfsfh, mode)
nfs_fchmod = _libnfs.nfs_fchmod

def nfs_chown(nfs, path, uid, gid):
    return _libnfs.nfs_chown(nfs, path, uid, gid)
nfs_chown = _libnfs.nfs_chown

def nfs_lchown(nfs, path, uid, gid):
    return _libnfs.nfs_lchown(nfs, path, uid, gid)
nfs_lchown = _libnfs.nfs_lchown

def nfs_fchown(nfs, nfsfh, uid, gid):
    return _libnfs.nfs_fchown(nfs, nfsfh, uid, gid)
nfs_fchown = _libnfs.nfs_fchown

def nfs_utimes(nfs, path, times):
    return _libnfs.nfs_utimes(nfs, path, times)
nfs_utimes = _libnfs.nfs_utimes

def nfs_lutimes(nfs, path, times):
    return _libnfs.nfs_lutimes(nfs, path, times)
nfs_lutimes = _libnfs.nfs_lutimes

def nfs_utime(nfs, path, times):
    return _libnfs.nfs_utime(nfs, path, times)
nfs_utime = _libnfs.nfs_utime

def nfs_access(nfs, path, mode):
    return _libnfs.nfs_access(nfs, path, mode)
nfs_access = _libnfs.nfs_access

def nfs_symlink(nfs, oldpath, newpath):
    return _libnfs.nfs_symlink(nfs, oldpath, newpath)
nfs_symlink = _libnfs.nfs_symlink

def nfs_rename(nfs, oldpath, newpath):
    return _libnfs.nfs_rename(nfs, oldpath, newpath)
nfs_rename = _libnfs.nfs_rename

def nfs_link(nfs, oldpath, newpath):
    return _libnfs.nfs_link(nfs, oldpath, newpath)
nfs_link = _libnfs.nfs_link

def mount_getexports(server):
    return _libnfs.mount_getexports(server)
mount_getexports = _libnfs.mount_getexports

def mount_free_export_list(exports):
    return _libnfs.mount_free_export_list(exports)
mount_free_export_list = _libnfs.mount_free_export_list

def nfs_find_local_servers():
    return _libnfs.nfs_find_local_servers()
nfs_find_local_servers = _libnfs.nfs_find_local_servers

def free_nfs_srvr_list(srv):
    return _libnfs.free_nfs_srvr_list(srv)
free_nfs_srvr_list = _libnfs.free_nfs_srvr_list
# This file is compatible with both classic and new-style classes.


