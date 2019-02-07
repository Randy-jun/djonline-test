import { shallowMount } from '@vue/test-utils'
import GroupManage from '@/components/GroupManage.vue'

describe('GroupManage.vue', () => {
  it('renders props.msg when passed', () => {
    const msg = 'new message'
    const wrapper = shallowMount(GroupManage, {
      propsData: { msg }
    })
    expect(wrapper.text()).toMatch(msg)
  })
})
