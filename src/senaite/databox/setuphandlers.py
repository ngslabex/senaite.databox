# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.DATABOX
#
# Copyright 2018 by it's authors.

from senaite.databox import logger


def setup_handler(context):
    """Generic setup handler
    """

    if context.readDataFile("senaite.databox.txt") is None:
        return

    logger.info("SENAITE.DATABOX setup handler [BEGIN]")
    portal = context.getSite()  # noqa
    add_databoxes_folder(portal)
    logger.info("SENAITE.DATABOX setup handler [DONE]")


def add_databoxes_folder(portal):
    """Adds the initial Databox folder
    """
    if portal.get("databoxes") is None:
        logger.info("Adding DataBox Folder")
        portal.invokeFactory("DataBoxFolder", "databoxes")


def post_install(portal_setup):
    """Runs after the last import step of the *default* profile

    This handler is registered as a *post_handler* in the generic setup profile

    :param portal_setup: SetupTool
    """
    logger.info("SENAITE.DATABOX install handler [BEGIN]")

    # https://docs.plone.org/develop/addons/components/genericsetup.html#custom-installer-code-setuphandlers-py
    profile_id = "profile-senaite.databox:default"
    context = portal_setup._getImportContext(profile_id)
    portal = context.getSite()  # noqa

    logger.info("SENAITE.DATABOX install handler [DONE]")


def post_uninstall(portal_setup):
    """Runs after the last import step of the *uninstall* profile

    This handler is registered as a *post_handler* in the generic setup profile

    :param portal_setup: SetupTool
    """
    logger.info("SENAITE.DATABOX uninstall handler [BEGIN]")

    # https://docs.plone.org/develop/addons/components/genericsetup.html#custom-installer-code-setuphandlers-py
    profile_id = "profile-senaite.databox:uninstall"
    context = portal_setup._getImportContext(profile_id)
    portal = context.getSite()  # noqa

    logger.info("SENAITE.DATABOX uninstall handler [DONE]")
