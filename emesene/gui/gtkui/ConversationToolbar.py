# -*- coding: utf-8 -*-

#    This file is part of emesene.
#
#    emesene is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    emesene is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with emesene; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import gtk

import gui
import utils

class ConversationToolbar(gtk.Toolbar):
    """
    A class that represents the toolbar on the conversation window
    """
    NAME = 'Conversation Toolbar'
    DESCRIPTION = 'The toolbar for a conversation'
    AUTHOR = 'Mariano Guerra'
    WEBSITE = 'www.emesene.org'

    def __init__(self, handler):
        """
        constructor

        handler -- an instance of e3common.Handler.ConversationToolbarHandler
        """
        gtk.Toolbar.__init__(self)
        self.set_style(gtk.TOOLBAR_ICONS)
        self.set_tooltips(True)

        toolbar_small = handler.session.config.get_or_set('b_toolbar_small', False)

        if toolbar_small:
            size = gtk.ICON_SIZE_MENU
        else:
            size = gtk.ICON_SIZE_LARGE_TOOLBAR

        whsize = gtk.icon_size_lookup(size)

        settings = self.get_settings()
        settings.set_long_property('gtk-toolbar-icon-size', size, \
            'ConversationToolbar.py:37')

        self.handler = handler

        # check if we have theme-specific toolbar-icons
        if gui.theme.toolbar_path:
            theme_tool_font = utils.safe_gtk_image_load(gui.theme.tool_font, whsize)
            theme_tool_font_color = utils.safe_gtk_image_load(gui.theme.tool_font_color, whsize)
            theme_tool_emotes = utils.safe_gtk_image_load(gui.theme.tool_emotes, whsize)
            theme_tool_nudge = utils.safe_gtk_image_load(gui.theme.tool_nudge, whsize)
            theme_tool_invite = utils.safe_gtk_image_load(gui.theme.tool_invite, whsize)
            theme_tool_clean = utils.safe_gtk_image_load(gui.theme.tool_clean, whsize)
            theme_tool_file_transfer = utils.safe_gtk_image_load(gui.theme.tool_file_transfer, whsize)
            theme_tool_ublock = utils.safe_gtk_image_load(gui.theme.tool_ublock, whsize)
        else:
            theme_tool_font = gtk.STOCK_SELECT_FONT
            theme_tool_font_color = gtk.STOCK_SELECT_COLOR
            theme_tool_emotes = utils.safe_gtk_image_load(gui.theme.emote_to_path(':D', True), whsize)
            theme_tool_nudge = utils.safe_gtk_image_load(gui.theme.emote_to_path(':S', True), whsize)
            theme_tool_invite = gtk.STOCK_ADD
            theme_tool_clean = gtk.STOCK_CLEAR
            theme_tool_file_transfer = gtk.STOCK_GO_UP
            theme_tool_ublock = gtk.STOCK_STOP

        theme_tool_call = utils.safe_gtk_image_load(gui.theme.call, whsize)
        theme_tool_video = utils.safe_gtk_image_load(gui.theme.video, whsize)
        theme_tool_av = utils.safe_gtk_image_load(gui.theme.av, whsize)

        self.font = gtk.ToolButton(theme_tool_font)
        self.font.set_label(_('Select font'))
        self.font.set_tooltip_text(_('Select font')) 
        self.font.connect('clicked',
            lambda *args: self.handler.on_font_selected())

        self.color = gtk.ToolButton(theme_tool_font_color)
        self.color.set_label(_('Select font color'))
        self.color.set_tooltip_text(_('Select font color')) 
        self.color.connect('clicked',
            lambda *args: self.handler.on_color_selected())

        self.emotes = gtk.ToolButton(theme_tool_emotes)
        self.emotes.set_label(_('Send an emoticon'))
        self.emotes.set_tooltip_text(_('Send an emoticon')) 
        self.emotes.connect('clicked',
            lambda *args: self.handler.on_emotes_selected())

        self.nudge = gtk.ToolButton(theme_tool_nudge)
        self.nudge.set_label(_('Request attention'))
        self.nudge.set_tooltip_text(_('Request attention')) 
        self.nudge.connect('clicked',
            lambda *args: self.handler.on_notify_attention_selected())

        self.invite = gtk.ToolButton(theme_tool_invite)
        self.invite.set_label(_('Invite a buddy'))
        self.invite.set_tooltip_text(_('Invite a buddy')) 
        self.invite.connect('clicked',
            lambda *args: self.handler.on_invite_selected())

        self.clean = gtk.ToolButton(theme_tool_clean)
        self.clean.set_label(_('Clean the conversation'))
        self.clean.set_tooltip_text(_('Clean the conversation')) 
        self.clean.connect('clicked',
            lambda *args: self.handler.on_clean_selected())

        self.invite_file_transfer = gtk.ToolButton(theme_tool_file_transfer)
        self.invite_file_transfer.set_label(_('Send a file'))
        self.invite_file_transfer.set_tooltip_text(_('Send a file')) 
        self.invite_file_transfer.connect('clicked',
            lambda *args: self.handler.on_invite_file_transfer_selected())

        self.ublock = gtk.ToolButton(theme_tool_ublock)
        self.ublock.set_label(_('Block/Unblock contact'))
        self.ublock.set_tooltip_text(_('Block/Unblock contact')) 
        self.ublock.connect('clicked',
            lambda *args: self.handler.on_ublock_selected())

        self.invite_video_call = gtk.ToolButton(theme_tool_video)
        self.invite_video_call.set_label(_('Video Call'))
        self.invite_video_call.set_tooltip_text(_('Video Call')) 
        self.invite_video_call.connect('clicked',
            lambda *args: self.handler.on_invite_video_call_selected())

        self.invite_audio_call = gtk.ToolButton(theme_tool_call)
        self.invite_audio_call.set_label(_('Voice Call'))
        self.invite_audio_call.set_tooltip_text(_('Voice Call')) 
        self.invite_audio_call.connect('clicked',
            lambda *args: self.handler.on_invite_voice_call_selected())

        self.invite_av_call = gtk.ToolButton(theme_tool_av)
        self.invite_av_call.set_label(_('Audio/Video Call'))
        self.invite_av_call.set_tooltip_text(_('Audio/Video Call')) 
        self.invite_av_call.connect('clicked',
            lambda *args: self.handler.on_invite_av_call_selected())

        self.add(self.font)
        self.add(self.color)
        self.add(gtk.SeparatorToolItem())

        self.add(self.emotes)
        self.add(self.nudge)
        self.add(gtk.SeparatorToolItem())

        self.add(self.invite)
        self.add(self.invite_file_transfer)
        self.add(gtk.SeparatorToolItem())

        #self.add(self.invite_video_call)
        #self.add(self.invite_audio_call)
        #self.add(self.invite_av_call)
        self.add(gtk.SeparatorToolItem())

        self.add(self.clean)
        self.add(self.ublock)
        self.add(gtk.SeparatorToolItem())

