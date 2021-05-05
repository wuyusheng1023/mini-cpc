import React, { useState, useEffect, useRef } from 'react';
import { w3cwebsocket as W3CWebSocket } from "websocket";

import Row from 'antd/lib/row';
import Col from 'antd/lib/col';
import Switch from 'antd/lib/switch';
import Tag from 'antd/lib/tag';
import List from 'antd/lib/list';

import {
  CloseCircleOutlined,
  ExclamationCircleOutlined,
} from '@ant-design/icons';

import TimeSeriesChart from './TimeSeriesChart.jsx';


const client = new W3CWebSocket("ws://localhost:8765");


export default function Dashboard() {
 
  const [running, setRunningg] = useState(false);
  const [warning, setWarning] = useState(false);
  const [error, setError] = useState(false);
  const [data, setData] = useState()

  client.onopen = () => {
    console.log("ws://localhost:8765");
  };

  client.onmessage = message => {
    const data = JSON.parse(message['data'])
    console.log(data);
    setData(data)
  };

  const onChangeRunning = checked => {
    setRunningg(checked);
  };

  return (
    <Row>
      <Col span={8} offset={0}>

        <Switch style={{ margin:5 }} onChange={onChangeRunning}/>

        {
          !running ? null :
            error ? 
              <Tag icon={<CloseCircleOutlined />} color="error">
                ERROR
              </Tag> :
              warning ? 
                <Tag icon={<ExclamationCircleOutlined />} color="warning">
                  WARNING
                </Tag>
                : null
        }

        {
          !running ? null :
            !data ? null:
              <>
                <h1 style={{ margin:10, padding:10, backgroundColor: "WhiteSmoke" }}>
                  <p style={{ fontSize: 35, display: "inline" }}>{data['concentration'].toPrecision(3)}</p>
                  <span>&nbsp;</span>
                  <p style={{ fontSize: 20, display: "inline" }}>#/cm<sup>3</sup></p>
                </h1>

                <Row>
                  <Col span={6} offset={2}>
                    <List
                      itemLayout="horizontal"
                      dataSource={['temp_sat', 'temp_con', 'temp_opt', 'flow']}
                      renderItem={item => (<List.Item>{item}</List.Item>)}
                    />
                  </Col>

                  <Col span={6} offset={2}>
                    <List
                      itemLayout="horizontal"
                      dataSource={[
                        data['saturator_temperature'].toFixed(2),
                        data['condensor_temperature'].toFixed(2),
                        data['optics_temperature'].toFixed(2),
                        data['flow'].toFixed(1),
                      ]}
                      renderItem={item => (<List.Item>{item}</List.Item>)}
                    />
                  </Col>

                  <Col span={6} offset={2}>
                    <List
                      itemLayout="horizontal"
                      dataSource={[
                        <text><sup>o</sup>C</text>,
                        <text><sup>o</sup>C</text>,
                        <text><sup>o</sup>C</text>,
                        <text>ml/min</text>,
                      ]}
                      renderItem={item => (<List.Item>{item}</List.Item>)}
                    />
                  </Col>
                </Row>
              </>            
        }


      </Col>
      <Col span={11} offset={0}>
        {
          !running ? 
            <h2 style={{color: "steelblue"}}>
              mini_CPC by University of Helsinki
            </h2>
            :
            // !data ? null :
              <>
                <TimeSeriesChart data={data}/>
              </>
        }
      </Col>
    </Row>
  );
};
