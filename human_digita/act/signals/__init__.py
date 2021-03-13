from django import dispatch

action_pre_save = dispatch.Signal(providing_args=["task"])
