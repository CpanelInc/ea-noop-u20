OBS_PROJECT := EA4
OBS_PACKAGE := ea-noop-u20
DISABLE_BUILD := repository=CentOS_6.5_standard repository=CentOS_7 repository=CentOS_8 repository=CentOS_9 repository=xUbuntu_22.04 repository=xUbuntu_24.04
include $(EATOOLS_BUILD_DIR)obs.mk
