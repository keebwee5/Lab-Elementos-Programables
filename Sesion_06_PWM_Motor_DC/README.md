# Control de motor DC con PWM

## PWM

**PWM (Pulse Width Modulation)** es una técnica para controlar la potencia promedio entregada al motor mediante pulsos digitales. En lugar de variar directamente el voltaje, se modifica el porcentaje de tiempo que la señal permanece encendida, conocido como **duty cycle**.

Un duty cycle bajo hace que el motor gire más lento, mientras que uno alto aumenta su velocidad. Por ejemplo, `0 %` mantiene el motor detenido, `50 %` entrega aproximadamente la mitad de la potencia promedio y `100 %` mantiene la señal activa todo el tiempo.

```text
25 %  ──        ──        ──
      └─────────┘ └─────────┘

50 %  ─────     ─────     ─────
          └─────┘   └─────┘

100 % ──────────────────────────
```

---

## IN1 / IN2 / ENA

En un puente H como el **L298N**, `IN1` e `IN2` controlan el **sentido de giro** del motor, mientras que `ENA` habilita el canal y recibe la señal PWM para controlar la **velocidad**.

```text
          ┌───────────────┐
IN1 ─────►│               │
IN2 ─────►│    PUENTE H   ├────► MOTOR DC
ENA ─────►│               │
          └───────────────┘
```

| IN1 | IN2 | Resultado |
|:---:|:---:|---|
| 0 | 0 | Motor detenido |
| 1 | 0 | Giro en un sentido |
| 0 | 1 | Giro contrario |

---

## Rampa

Una **rampa** consiste en aumentar o reducir el PWM de forma gradual. En lugar de pasar instantáneamente de `0 %` a `100 %`, la velocidad cambia poco a poco.

```text
PWM

100 %             ───────
                 /
               /
             /
0 % ────────
          tiempo →
```

Esto permite arranques y frenados más suaves, reduce movimientos bruscos y disminuye los picos de corriente que aparecen cuando el motor cambia de velocidad repentinamente.

---

## Cambio seguro de dirección

No es recomendable invertir directamente `IN1` e `IN2` mientras el motor todavía está girando, ya que la inercia del motor puede provocar picos de corriente, vibraciones y esfuerzo mecánico.

La forma segura es **reducir primero el PWM hasta 0**, esperar un instante, cambiar `IN1` e `IN2` y después volver a aumentar el PWM con una rampa.

```mermaid
flowchart LR
    A[Motor girando] --> B[Reducir PWM]
    B --> C[PWM = 0]
    C --> D[Cambiar IN1 / IN2]
    D --> E[Aumentar PWM]
    E --> F[Giro contrario]
```

---

## Tabla de pruebas

| Prueba | Resultado esperado |
|---|---|
| PWM = 0 % | Motor detenido |
| PWM = 50 % | Velocidad media |
| PWM = 100 % | Velocidad máxima |
| IN1=1 / IN2=0 | Giro en un sentido |
| IN1=0 / IN2=1 | Giro contrario |
| Rampa 0 → 100 % | Aceleración progresiva |
| Rampa 100 → 0 % | Frenado progresivo |
| Cambio de dirección | Se detiene antes de invertir |

---

## Problemas encontrados

Uno de los principales problemas fue que con valores muy bajos de PWM el motor podía vibrar sin comenzar a girar, debido a que no tenía suficiente fuerza para vencer la fricción inicial. También se observó que un cambio directo de dirección producía movimientos demasiado bruscos.

Para solucionarlo se utilizó un **PWM mínimo efectivo**, rampas de aceleración y desaceleración, y una secuencia segura para invertir el sentido de giro. También es importante utilizar una fuente capaz de entregar la corriente necesaria y revisar que el driver no se caliente excesivamente.

---

## Resumen

```text
IN1 + IN2  → Dirección
ENA + PWM  → Velocidad
Rampa      → Movimiento suave
PWM = 0    → Paso previo para invertir dirección
```
