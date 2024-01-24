/** @odoo-module **/

import { AttendeeCalendarCommonPopover } from "@calendar/views/attendee_calendar/common/attendee_calendar_common_popover";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";

patch(AttendeeCalendarCommonPopover.prototype, 'lt_calendar_navigation.calendar_enhancement_patch', {
    async onClickNavigateTo() {
        window.location.href = _.str.sprintf(this.env._t('https://www.google.com/maps/search/?api=1&query=%s'), this.props.record.rawRecord.location);
    }
})
