#region Using Directives

using System.Drawing;
using System.Security.Permissions;
using System.Windows.Forms;
using ARCed.Core.Win32;

#endregion

namespace ARCed.UI
{
	public abstract class DockPaneCaptionBase : Control
	{
		protected internal DockPaneCaptionBase(DockPane pane)
		{
			this._mDockPane = pane;

			SetStyle(ControlStyles.OptimizedDoubleBuffer |
                ControlStyles.ResizeRedraw |
                ControlStyles.UserPaint |
                ControlStyles.AllPaintingInWmPaint, true);
			SetStyle(ControlStyles.Selectable, false);
		}

        private readonly DockPane _mDockPane;
		protected DockPane DockPane
		{
			get	{	return this._mDockPane;	}
		}

		protected DockPane.AppearanceStyle Appearance
		{
			get	{	return this.DockPane.Appearance;	}
		}

        protected bool HasTabPageContextMenu
        {
            get { return this.DockPane.HasTabPageContextMenu; }
        }

        protected void ShowTabPageContextMenu(Point position)
        {
            this.DockPane.ShowTabPageContextMenu(this, position);
        }

        protected override void OnMouseUp(MouseEventArgs e)
        {
            base.OnMouseUp(e);

            if (e.Button == MouseButtons.Right)
                this.ShowTabPageContextMenu(new Point(e.X, e.Y));
        }

        protected override void OnMouseDown(MouseEventArgs e)
        {
            base.OnMouseDown(e);

            if (e.Button == MouseButtons.Left &&
			    this.DockPane.DockPanel.AllowEndUserDocking &&
                this.DockPane.AllowDockDragAndDrop &&
				!DockHelper.IsDockStateAutoHide(this.DockPane.DockState) &&
                this.DockPane.ActiveContent != null)
				this.DockPane.DockPanel.BeginDrag(this.DockPane);
        }

        [SecurityPermission(SecurityAction.LinkDemand, Flags = SecurityPermissionFlag.UnmanagedCode)]         
        protected override void WndProc(ref Message m)
        {
            if (m.Msg == (int)Msgs.WM_LBUTTONDBLCLK)
            {
                if (DockHelper.IsDockStateAutoHide(this.DockPane.DockState))
                {
                    this.DockPane.DockPanel.ActiveAutoHideContent = null;
                    return;
                }

                if (this.DockPane.IsFloat)
                    this.DockPane.RestoreToPanel();
                else
                    this.DockPane.Float();
            }
            base.WndProc(ref m);
        }

		internal void RefreshChanges()
		{
            if (IsDisposed)
                return;

			this.OnRefreshChanges();
		}

        protected virtual void OnRightToLeftLayoutChanged()
        {
        }

		protected virtual void OnRefreshChanges()
		{
		}

		protected internal abstract int MeasureHeight();
	}
}
