/* All code in this file Copyright G Himangi
 * Downloaded from http://www.codeproject.com/useritems/flagenumeditor.asp
 * Modified the Namespace just because it was too generic.
 * Added DesignTimeVisible(false) to hide it from the toolbox.
 */

#region Using Directives

using System;
using System.ComponentModel;
using System.Drawing.Design;
using System.Windows.Forms;
using System.Windows.Forms.Design;

#endregion

namespace ARCed.Scintilla.Design
{
    [DesignTimeVisible(false)]
    public class FlagCheckedListBox : CheckedListBox
    {
        private readonly Container components = null;

        public FlagCheckedListBox()
        {
            // This call is required by the Windows.Forms Form Designer.
            this.InitializeComponent();

            // TODO: Add any initialization after the InitForm call

        }

        protected override void Dispose(bool disposing)
        {
            if(disposing)
            {
                if(this.components != null)
                    this.components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Component Designer generated code
        private void InitializeComponent()
        {
            // 
            // FlaggedCheckedListBox
            // 
            this.CheckOnClick = true;

        }
        #endregion

        // Adds an integer value and its associated description
        public FlagCheckedListBoxItem Add(int v, string c)
        {
            var item = new FlagCheckedListBoxItem(v, c);
            Items.Add(item);
            return item;
        }

        public FlagCheckedListBoxItem Add(FlagCheckedListBoxItem item)
        {
            Items.Add(item);
            return item;
        }

        protected override void OnItemCheck(ItemCheckEventArgs e)
        {
            base.OnItemCheck(e);

            if(this.isUpdatingCheckStates)
                return;

            // Get the checked/unchecked item
            var item = Items[e.Index] as FlagCheckedListBoxItem;
            // Update other items
            this.UpdateCheckedItems(item, e.NewValue);
        }

        // Checks/Unchecks items depending on the give bitvalue
        protected void UpdateCheckedItems(int value)
        {

            this.isUpdatingCheckStates = true;

            // Iterate over all items
            for(int i=0; i<Items.Count; i++)
            {
                var item = Items[i] as FlagCheckedListBoxItem;

                if(item.value==0)
                {
                    SetItemChecked(i, value==0);
                }
                else
                {

                    // If the bit for the current item is on in the bitvalue, check it
                    if((item.value & value)== item.value && item.value!=0)
                        SetItemChecked(i, true);
                    // Otherwise uncheck it
                    else
                        SetItemChecked(i, false);
                }
            }

            this.isUpdatingCheckStates = false;

        }

        // Updates items in the checklistbox
        // composite = The item that was checked/unchecked
        // cs = The check state of that item
        protected void UpdateCheckedItems(FlagCheckedListBoxItem composite, CheckState cs)
        {

            // If the value of the item is 0, call directly.
            if(composite.value==0)
                this.UpdateCheckedItems(0);


            // Get the total value of all checked items
            int sum = 0;
            for(int i=0; i<Items.Count; i++)
            {
                var item = Items[i] as FlagCheckedListBoxItem;

                // If item is checked, add its value to the sum.
                if(GetItemChecked(i))
                    sum |= item.value;
            }

            // If the item has been unchecked, remove its bits from the sum
            if(cs==CheckState.Unchecked)
                sum = sum & (~composite.value);
            // If the item has been checked, combine its bits with the sum
            else
                sum |= composite.value;

            // Update all items in the checklistbox based on the final bit value
            this.UpdateCheckedItems(sum);

        }

        private bool isUpdatingCheckStates;

        // Gets the current bit value corresponding to all checked items
        public int GetCurrentValue()
        {
            int sum = 0;

            for(int i=0; i<Items.Count; i++)
            {
                var item = Items[i] as FlagCheckedListBoxItem;

                if(GetItemChecked(i))
                    sum |= item.value;
            }

            return sum;
        }

        Type enumType;
        Enum enumValue;

        // Adds items to the checklistbox based on the members of the enum
        private void FillEnumMembers()
        {
            foreach(string name in Enum.GetNames(this.enumType))
            {
                object val = Enum.Parse(this.enumType, name);
                var intVal = (int)Convert.ChangeType(val, typeof(int));

                this.Add(intVal, name);
            }
        }

        // Checks/unchecks items based on the current value of the enum variable
        private void ApplyEnumValue()
        {
            var intVal = (int)Convert.ChangeType(this.enumValue, typeof(int));
            this.UpdateCheckedItems(intVal);

        }

        [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public Enum EnumValue
        {
            get
            {
                object e = Enum.ToObject(this.enumType, this.GetCurrentValue());
                return (Enum)e;
            }
            set
            {

                Items.Clear();
                this.enumValue = value; // Store the current enum value
                this.enumType = value.GetType(); // Store enum type
                this.FillEnumMembers(); // Add items for enum members
                this.ApplyEnumValue(); // Check/uncheck items depending on enum value

            }
        }


    }

    // Represents an item in the checklistbox
    public class FlagCheckedListBoxItem
    {
        public FlagCheckedListBoxItem(int v, string c)
        {
            this.value = v;
            this.caption = c;
        }

        public override string ToString()
        {
            return this.caption;
        }

        // Returns true if the value corresponds to a single bit being set
        public bool IsFlag
        {
            get
            {
                return ((this.value & (this.value - 1)) == 0);
            }
        }

        // Returns true if this value is a member of the composite bit value
        public bool IsMemberFlag(FlagCheckedListBoxItem composite)
        {
            return (this.IsFlag && ((this.value & composite.value) == this.value));
        }

        public int value;
        public string caption;
    }


    // UITypeEditor for flag enums
    public class FlagEnumUIEditor : UITypeEditor
    {
        // The checklistbox
        private readonly FlagCheckedListBox flagEnumCB;

        public FlagEnumUIEditor()
        {
            this.flagEnumCB = new FlagCheckedListBox
            {
                BorderStyle = BorderStyle.None
            };
        }

        public override object EditValue(ITypeDescriptorContext context, IServiceProvider provider, object value)
        {
            if(context != null
                && context.Instance != null
                && provider != null)
            {

                var edSvc = (IWindowsFormsEditorService)provider.GetService(typeof(IWindowsFormsEditorService));

                if(edSvc != null)
                {

                    var e = (Enum)Convert.ChangeType(value, context.PropertyDescriptor.PropertyType);
                    this.flagEnumCB.EnumValue = e;
                    edSvc.DropDownControl(this.flagEnumCB);
                    return this.flagEnumCB.EnumValue;

                }
            }
            return null;
        }

        public override UITypeEditorEditStyle GetEditStyle(ITypeDescriptorContext context)
        {
            return UITypeEditorEditStyle.DropDown;
        }


    }

}
