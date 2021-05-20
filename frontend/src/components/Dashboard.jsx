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
import useInterval from '../hooks/useInterval.jsx';


const ws = "ws://localhost:8765"
let client = new W3CWebSocket(ws);


export default function Dashboard() {

  const hostname = window.location.hostname;
  const port = window.location.port;
  const urlCommand = `http://${hostname}:${port}/api/command`;

  const [running, setRunning] = useState(true);
  const [warning, setWarning] = useState(false);
  const [error, setError] = useState(false);
  const [data, setData] = useState();
  const [dataArr, setDataArr] = useState([]);
  const [datetime,setDatetime] = useState(Date.now());

  useEffect(() => {
    const data = running ? 'on' : 'off';
    fetch(urlCommand, {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: JSON.stringify(data),
    })
      .then(res => res.json())
      .then(res => console.log('Post res:', res))
      .catch(console.error);
  }, [running])

  // client.onopen = () => {
  //   console.log("ws://localhost:8765");
  // };

  const onMessage = message => {
    const data = JSON.parse(message['data'])
    console.log(data);
    setData(data);
    setDatetime(Date.now())
  };

  client.onmessage = onMessage;

  useInterval(() => {
    if ((Date.now() - datetime) > 2000) {
      client = new W3CWebSocket(ws);
      client.onmessage = onMessage;
    } else {
      const datetime = new Date();
      const newData = {...data};
      newData['datetime'] = datetime;
      const newDataArr = [...dataArr];
      newDataArr.push(newData);
      while ((Date.parse(datetime) - Date.parse(newDataArr[0]['datetime'])) >= 60 * 60 * 1000) {
        newDataArr.shift();
      };
      setDataArr(newDataArr);
    };
  }, 2000);

  const onChangeRunning = checked => {
    setRunning(checked);
  };

  return (
    <Row>
      <Col span={8} offset={0}>

        <Switch
          style={{ margin: 5 }}
          defaultChecked={true}
          onChange={onChangeRunning}
        />
        
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
                        parseFloat(data['saturator_temperature']).toFixed(2),
                        parseFloat(data['condensor_temperature']).toFixed(2),
                        parseFloat(data['optics_temperature']).toFixed(2),
                        parseFloat(data['sample_flow']).toFixed(2),
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
            <TimeSeriesChart dataArr={dataArr}/>
        }
      </Col>
    </Row>
  );
};
