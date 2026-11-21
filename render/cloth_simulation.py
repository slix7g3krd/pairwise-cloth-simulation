import math

def substeps(dt, max_step):
    """固定子步。"""
    raise NotImplementedError("TODO: substeps")

def constraint_iterations(error, base):
    """约束迭代。"""
    raise NotImplementedError("TODO: constraint_iterations")

def wind_scale(wind, factor):
    """风场缩放。"""
    raise NotImplementedError("TODO: wind_scale")

def hash_cell(position, size):
    """自碰撞哈希。"""
    raise NotImplementedError("TODO: hash_cell")

def pinned_target(current, bone):
    """固定点跟随骨骼。"""
    raise NotImplementedError("TODO: pinned_target")

def friction(tangential, mu):
    """摩擦。"""
    raise NotImplementedError("TODO: friction")

def lod_state(level, state):
    """LOD 状态。"""
    raise NotImplementedError("TODO: lod_state")

def readback_interp(prev, cur, alpha):
    """回读插值。"""
    raise NotImplementedError("TODO: readback_interp")

def pause_wind(wind, paused):
    """暂停冻结。"""
    raise NotImplementedError("TODO: pause_wind")

def stretch_ratio(length, rest):
    """拉伸比。"""
    raise NotImplementedError("TODO: stretch_ratio")

def integrate(position, velocity, dt):
    """积分。"""
    raise NotImplementedError("TODO: integrate")

def damping(velocity, k):
    """阻尼。"""
    raise NotImplementedError("TODO: damping")

def collision_time(t, dt):
    """连续碰撞时间。"""
    raise NotImplementedError("TODO: collision_time")

def rest_length(length, scale):
    """静止长度。"""
    raise NotImplementedError("TODO: rest_length")

def cloth_id(seed, index):
    """布料 id。"""
    raise NotImplementedError("TODO: cloth_id")
