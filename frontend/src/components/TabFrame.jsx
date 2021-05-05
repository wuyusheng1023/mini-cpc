import React, { useState } from 'react';
import Tabs from 'antd/lib/tabs';

import Dashboard from './Dashboard.jsx';

const { TabPane } = Tabs;


export default function TabFrame() {

  return (
    <Tabs type="card" defaultActiveKey="1">
      <TabPane tab="Dashboard" key="1">
        <Dashboard />
      </TabPane>

      <TabPane tab="Setting" key="2">
        2
      </TabPane>
    </Tabs>
  );
};
