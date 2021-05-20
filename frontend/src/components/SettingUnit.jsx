import React, { useState, useEffect } from 'react';

import Button from 'antd/lib/button';
import Tag from 'antd/lib/tag';
import {
  CaretUpOutlined,
  CaretDownOutlined
} from '@ant-design/icons';


export default function SettingUnit({
  defaultName,
  defaultValue,
  delta,
  onChange = f => f,
}) {
  const [name, setName] = useState(defaultName)
  const [value, setValue] = useState(defaultValue)

  useEffect(() => {
    setValue(defaultValue);
  }, [defaultValue])

  useEffect(() => {
    onChange(value);
  }, [value])

  const increase = () => {
    if (delta >= 1) {
      const newValue = parseInt(value) + parseInt(delta);
      setValue(newValue);
    } else {
      const newValue = parseFloat(value) + parseFloat(delta);
      setValue(parseFloat(newValue.toFixed(2)));
    };
  };

  const decrease = () => {
    if (delta >= 1) {
      const newValue = parseInt(value) - parseInt(delta);
      setValue(newValue);
    } else {
      const newValue = parseFloat(value) - parseFloat(delta);
      setValue(parseFloat(newValue.toFixed(2)));
    };
  };

  return (
    <div style={{ width: 75, height: 200 }}>
      <Tag style={{ width: 75, height: 40 }}>{name}</Tag>
      <Button
        style={{ width: 75, height: 40 }}
        icon={<CaretUpOutlined />}
        onClick={increase}
      />
      <Tag style={{ width: 75, height: 40 }}>{value}</Tag>
      <Button
        style={{ width: 75, height: 40 }}
        icon={<CaretDownOutlined />}
        onClick={decrease}
      />
    </div>
  )
};
