import wx

from Boot import WelderImport

Kernel = WelderImport('Kernel')
Core = WelderImport('Core')
KM = Kernel.Manager

Templates = Core.Database.Welder_Templates
DM = Core.Database.Manager
RPG = Core.RMXP.RGSS1_RPG.RPG

ChooseGraphic_Dialog = Core.Database.Dialogs.ChooseGraphic_Dialog

PanelBase = Core.Panels.PanelBase
#--------------------------------------------------------------------------------------
# Skills_Panel
#--------------------------------------------------------------------------------------

class Skills_Panel( Templates.Skills_Panel, PanelBase):

    _arc_panel_info_string = "Name Caption Center CloseB CaptionV DestroyOC Floatable Float IconARCM MaximizeB MinimizeM MinimizeB Movable NotebookD Resizable Snappable"
    _arc_panel_info_data = {"Name": "Skills Panel", "Caption": "Skills Panel", "CaptionV": True,  "MinimizeM": ["POS_SMART", "CAPT_SMART",], 
                            "MinimizeB": True, "CloseB": True, 'IconARCM': 'skillsicon'}

    def __init__( self, parent, skill_index=0 ):
        Templates.Skills_Panel.__init__( self, parent )
        global Config, DataSkills, DataAnimations, DataElements
        global DataStates, DataCommonEvents
        Config = Kernel.GlobalObjects.get_value('Welder_config')
        try:
            proj = Kernel.GlobalObjects.get_value('PROJECT')
            DataSkills = proj.getData('Skills')
            DataAnimations = proj.getData('Animations')
            DataStates = proj.getData('States')
            DataElements = proj.getData('System').elements
            DataCommonEvents = proj.getData('CommonEvents')
        except NameError:
            Kernel.Log('Database opened before Project has been initialized', '[Database:SKILLS]', True)
            self.Destroy()
        font = wx.Font(8, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        font.SetFaceName(Config.get('Misc', 'NoteFont')) 
        self.textCtrlNotes.SetFont(font)
        DM.DrawButtonIcon(self.bitmapButtonAudioTest, 'play_button', True)
        self.comboBoxMenuSE.SetCursor(wx.STANDARD_CURSOR)

        default = ['SP Cost:', 'Power:', 'Variance:', 'Hit Rate:', 
            'ATK-F:', 'PDEF-F:', 'MDEF-F:', 'EVA-F:']
        self.ParameterControls = DM.CreateParameterControls(self.panelParameters, 
            self.spinCtrlParameter_ValueChanged, '-F:', 4, default)

        self.setRanges()
        self.SelectedSkill = DataSkills[DM.FixedIndex(skill_index)]
        self.refreshAll()
        self.listBoxSkills.SetSelection(skill_index)
        DM.DrawHeaderBitmap(self.bitmapSkills, 'Skills')

        # Bind the panel to the Panel Manager
        self.BindPanelManager()

    def refreshSkillList( self ):
        """Refreshes the values in the skill wxListBox control"""
        digits = len(Config.get('GameObjects', 'Skills'))
        DM.FillControl(self.listBoxSkills, DataSkills, digits, [])

    def refreshAnimations( self ):
        """Refreshes the choices in the user and target animation controls"""
        digits = len(Config.get('GameObjects', 'Animations'))
        DM.FillControl(self.comboBoxTargetAnimation, DataAnimations, digits, ['(None)'])
        DM.FillControl(self.comboBoxUserAnimation, DataAnimations, digits, ['(None)'])

    def refreshElements( self ):
        """Clears and refreshes the list of elements in the checklist"""
        self.checkListElements.Clear()
        self.checkListElements.AppendItems(DataElements[DM.FixedIndex(0):])

    def refreshStates( self ):
        """Clears and refreshes the list of states in the checklist"""
        self.checkListStates.DeleteAllItems()
        names = [DataStates[i].name for i in xrange(DM.FixedIndex(0), len(DataStates))]
        self.checkListStates.AppendItems(names)

    def refreshCommonEvents( self ):
        """Refreshes the common events in the combo box"""
        digits = len(Config.get('GameObjects', 'CommonEvents'))
        DM.FillControl(self.comboBoxCommonEvent, DataCommonEvents, digits, ['(None)'])

    def refreshValues(self ):
        """Resets the values of all the controls to reflect the selected skill"""
        skill = self.SelectedSkill
        self.textCtrlName.ChangeValue(skill.name)
        self.textCtrlDescription.ChangeValue(skill.description)
        self.labelIconName.SetLabel(skill.icon_name)
        DM.DrawButtonIcon(self.bitmapButtonIcon, skill.icon_name, False)
        self.comboBoxScope.SetSelection(skill.scope)
        self.comboBoxOccasion.SetSelection(skill.occasion)
        self.comboBoxUserAnimation.SetSelection(skill.animation1_id)
        self.comboBoxTargetAnimation.SetSelection(skill.animation2_id)
        self.comboBoxCommonEvent.SetSelection(skill.common_event_id)
        self.comboBoxMenuSE.SetValue(skill.menu_se.name)

        # TODO: Remove this. Something got screwed up with the conversion
        if skill.power > 2147483647:
            skill.power = 0

        if DM.ARC_FORMAT:
            # TODO: Implement
            pass
        else:
            self.ParameterControls[0].SetValue(skill.sp_cost)
            self.ParameterControls[1].SetValue(skill.power) 
            self.ParameterControls[2].SetValue(skill.hit)
            self.ParameterControls[3].SetValue(skill.variance)
            self.ParameterControls[4].SetValue(skill.atk_f)
            self.ParameterControls[5].SetValue(skill.pdef_f)
            self.ParameterControls[6].SetValue(skill.mdef_f)
            self.ParameterControls[7].SetValue(skill.eva_f)		
            self.ParameterControls[8].SetValue(skill.str_f)
            self.ParameterControls[9].SetValue(skill.dex_f)
            self.ParameterControls[10].SetValue(skill.agi_f)
            self.ParameterControls[11].SetValue(skill.int_f)
        # Update elements
        for i in xrange(self.checkListElements.GetItemCount()):
            checked = skill.element_set
            if not DM.ARC_FORMAT:
                checked = [i - 1 for i in checked]
            self.checkListElements.SetChecked(checked)
        # Update plus/minus states
        if DM.ARC_FORMAT:
            addstates = skill.plus_state_set
            minusstates = skill.minus_state_set
        else:
            addstates = [id - 1 for id in skill.plus_state_set]
            minusstates = [id - 1 for id in skill.minus_state_set]
        for i in xrange(self.checkListStates.GetItemCount()):
            if i in addstates:
                self.checkListStates.SetItemImage(i, 1)
            elif i in minusstates:
                self.checkListStates.SetItemImage(i, 2)
            else:
                self.checkListStates.SetItemImage(i, 0)
        # RMXP Compatibility
        if not hasattr(skill, 'note'):
            setattr(skill, 'note', '')
        self.textCtrlNotes.ChangeValue(skill.note)

    def refreshAll( self ):
        """Refreshes all child controls of the panel"""
        self.refreshSkillList()
        self.refreshAnimations()
        self.refreshStates()
        self.refreshElements()
        self.refreshCommonEvents()
        self.refreshValues()

    def setRanges( self ):
        self.ParameterControls[0].SetRange(0, Config.getint('DatabaseLimits', 'ActorSP'))
        max = Config.getint('DatabaseLimits', 'ActorParameter')
        self.ParameterControls[1].SetRange(-max, max)
        for i in xrange(2, len(self.ParameterControls)):
            self.ParameterControls[i].SetRange(0, max)

    def listBoxSkills_SelectionChanged( self, event ):
        """Changes the selected skill and update the values on the panel"""
        index = DM.FixedIndex(event.GetSelection())
        if DataSkills[index] == None:
            DataSkills[index] = RPG.Skill()
        self.SelectedSkill = DataSkills[index]
        self.refreshValues()

    def buttonMaximum_Clicked( self, event ):
        """Starts the Change Maximum dialog"""
        max = Config.getint('GameObjects', 'Skills')
        DM.ChangeDataCapacity(self, self.listBoxSkills, DataSkills, max)

    def textCtrlName_TextChanged( self, event ):
        """Updates the selected skill's name"""
        DM.UpdateObjectName(self.SelectedSkill, event.GetString(),
            self.listBoxSkills, len(Config.get('GameObjects', 'Skills')))

    def bitmapButtonIcon_Clicked( self, event ):
        """Opens dialog to select an icon for the selected skill"""
        filename = DM.ChooseGraphic(self, 'Icons', self.SelectedSkill.icon_name)
        if filename:
            self.SelectedSkill.icon_name = filename
        self.refreshValues()

    def bitmapButtonAudioTest_Clicked( self, event ):
        """Plays the sound effect as a quick test without opening the dialog"""
        DM.QuickPlay(self.SelectedSkill.menu_se, 'SE')

    def textCtrlDescription_TextChange( self, event ):
        """Set the selected skill's description"""
        self.SelectedSkill.description = event.GetString()

    def comboBoxScope_SelectionChanged( self, event ):
        """Set the selected skill's scope"""
        self.SelectedSkill.scope = event.GetInt()

    def comboBoxUserAnimation_SelectionChanged( self, event ):
        """Set the selected skill's user animation ID"""
        self.SelectedSkill.animation1_id = event.GetInt()

    def comboBoxMenuSE_Clicked( self, event ):
        """Opens the dialog for selecting the audio file to use"""
        audio = DM.ChooseAudio(self, self.SelectedSkill.menu_se, 'SE')
        if audio:
            self.SelectedSkill.menu_se = audio
            self.comboBoxMenuSE.SetValue(audio.name)

    def comboBoxOccasion_SelectionChanged( self, event ):
        """Set the selected skill's occasion"""
        self.SelectedSkill.occasion = event.GetInt()

    def comboBoxTargetAnimation_SelectionChanged( self, event ):
        """Set the selected skill's target animation ID"""
        self.SelectedSkill.animation2_id = event.GetInt()

    def comboBoxCommonEvent_SelectionChanged( self, event ):
        """Set the selected skill's SP cost"""
        self.SelectedSkill.common_event_id = event.GetInt()

    def spinCtrlParameter_ValueChanged( self, event ):
        index = self.ParameterControls.index(event.GetEventObject())
        skill = self.SelectedSkill
        if DM.ARC_FORMAT:
            # TODO: Implement
            pass
        else:
            value = event.GetInt()
            if index == 0: skill.sp_cost = value
            elif index == 1: skill.power = value
            elif index == 2: skill.variance = value
            elif index == 3: skill.hit_rate = value
            elif index == 4: skill.atk_f = value
            elif index == 5: skill.pdef_f = value
            elif index == 6: skill.mdef_f = value
            elif index == 7: skill.eva_f = value
            elif index == 8: skill.str_f = value
            elif index == 9: skill.dex_f = value
            elif index == 10: skill.agi_f = value
            elif index == 11: skill.int_f = value

    def textCtrlNotes_TextChanged( self, event ):
        """Sets the note for the selected skill"""
        self.SelectedSkill.note = event.GetString()

    def checkListElements_Clicked( self, event ):
        """Updates the element set for the selected skill"""
        self.checkListElements.ChangeState(event, 1)
        if DM.ARC_FORMAT:
            # TODO: Implement
            pass
        else:
            ids = [DM.FixedIndex(id) for id in self.checkListElements.GetChecked()]
            self.SelectedSkill.element_set = ids

    def checkListStates_LeftClicked( self, event ):
        """Updates the plus/minus state set for the selected skill"""
        data = self.checkListStates.ChangeState(event, 1)
        DM.ChangeSkillStates(self.SelectedSkill, data[0], data[1])

    def checkListStates_RigthClicked( self, event ):
        """Updates the plus/minus state set for the selected skill"""
        data = self.checkListStates.ChangeState(event, -1)
        DM.ChangeSkillStates(self.SelectedSkill, data[0], data[1])