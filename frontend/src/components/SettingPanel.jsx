import React, { useState, useEffect } from 'react';

import Row from 'antd/lib/row';
import Col from 'antd/lib/col';
import Button from 'antd/lib/button'

import SettingUnit from './SettingUnit.jsx';


export default function SettingPanel() {
  
  const hostname = window.location.hostname;
  const port = window.location.port;
  const urlSettings = `http://${hostname}:${port}/api/settings`;
  const urlSet = `http://${hostname}:${port}/api/set`;

  const [satTDefault, setSatTDefault] = useState();
  const [conTDefault, setConTDefault] = useState();
  const [optTDefault, setOptTDefault] = useState();
  const [flowDefault, setFlowDefault] = useState();
  const [satT, setSatT] = useState();
  const [conT, setConT] = useState();
  const [optT, setOptT] = useState();
  const [flow, setFlow] = useState();

  const setAll = settings => {
    setSatTDefault(settings['saturator_temperature']);
    setConTDefault(settings['condensor_temperature']);
    setOptTDefault(settings['optics_temperature']);
    setFlowDefault(settings['sample_flow']);
  };

  useEffect( () => {
    fetch(urlSettings)
      .then(res => res.json())
      .then(setAll)
      .catch(console.error);
  }, []);

  const onChangeSat = value => {
    setSatT(value);
  };

  const onChangeCon = value => {
    setConT(value);
  };

  const onChangeOpt = value => {
    setOptT(value);
  };

  const onChangeFlow = value => {
    setFlow(value);
  };

  const onSubmit = () => {
    const data = {
      'saturator_temperature': satT,
      'condensor_temperature': conT,
      'optics_temperature': optT,
      'sample_flow': flow,
    };
    fetch(urlSet, {
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
  };

  return (
    <>
      <Row>
        <Col>
          <SettingUnit
            defaultName={'Sat_T'}
            defaultValue={satTDefault ? satTDefault : 50}
            delta={1}
            onChange={onChangeSat}
          />
        </Col>
        <Col>
          <SettingUnit
            defaultName={'Con_T'}
            defaultValue={conTDefault ? conTDefault : 20}
            delta={1}
            onChange={onChangeCon}
          />
        </Col>
        <Col>
          <SettingUnit
            defaultName={'Opt_T'}
            defaultValue={optTDefault ? optTDefault : 50}
            delta={1}
            onChange={onChangeOpt}
          />
        </Col>
        <Col>
          <SettingUnit
            defaultName={'flow'}
            defaultValue={flowDefault ? flowDefault : 0.1}
            delta={0.01}
            onChange={onChangeFlow}
          />
        </Col>
      </Row>
      <Row>
        <Button onClick={onSubmit}>Confirm</Button>
      </Row>
    </>
  )
};
