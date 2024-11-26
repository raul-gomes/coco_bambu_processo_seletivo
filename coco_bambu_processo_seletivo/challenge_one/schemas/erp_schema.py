from sqlalchemy import (
    Column, Integer, String, Float, Boolean, ForeignKey, DateTime, create_engine
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# Tabela de Guest Checks
class GuestCheck(Base):
    __tablename__ = 'guest_checks'

    guest_check_id = Column(Integer, primary_key=True)
    chk_num = Column(Integer, nullable=False)
    opn_bus_dt = Column(String, nullable=False)
    opn_utc = Column(DateTime, nullable=False)
    opn_lcl = Column(DateTime, nullable=False)
    clsd_bus_dt = Column(String, nullable=False)
    clsd_utc = Column(DateTime, nullable=False)
    clsd_lcl = Column(DateTime, nullable=False)
    last_trans_utc = Column(DateTime, nullable=False)
    last_trans_lcl = Column(DateTime, nullable=False)
    last_updated_utc = Column(DateTime, nullable=False)
    last_updated_lcl = Column(DateTime, nullable=False)
    clsd_flag = Column(Boolean, nullable=False)
    gst_cnt = Column(Integer, nullable=False)
    sub_ttl = Column(Float, nullable=False)
    non_txbl_sls_ttl = Column(Float, nullable=True)
    chk_ttl = Column(Float, nullable=False)
    dsc_ttl = Column(Float, nullable=False)
    pay_ttl = Column(Float, nullable=False)
    bal_due_ttl = Column(Float, nullable=True)
    rvc_num = Column(Integer, nullable=False)
    ot_num = Column(Integer, nullable=False)
    oc_num = Column(Integer, nullable=True)
    tbl_num = Column(Integer, nullable=False)
    tbl_name = Column(String, nullable=False)
    emp_num = Column(Integer, nullable=False)
    num_srvc_rd = Column(Integer, nullable=False)
    num_chk_prntd = Column(Integer, nullable=False)

    # Relações
    taxes = relationship("Tax", back_populates="guest_check")
    detail_lines = relationship("DetailLine", back_populates="guest_check")

# Tabela de Taxes
class Tax(Base):
    __tablename__ = 'taxes'

    id = Column(Integer, primary_key=True)
    tax_num = Column(Integer, nullable=False)
    txbl_sls_ttl = Column(Float, nullable=False)
    tax_coll_ttl = Column(Float, nullable=False)
    tax_rate = Column(Float, nullable=False)
    type = Column(Integer, nullable=False)
    guest_check_id = Column(Integer, ForeignKey('guest_checks.guest_check_id'))

    # Relação inversa
    guest_check = relationship("GuestCheck", back_populates="taxes")

# Tabela de Detail Lines
class DetailLine(Base):
    __tablename__ = 'detail_lines'

    guest_check_line_item_id = Column(Integer, primary_key=True)
    rvc_num = Column(Integer, nullable=False)
    dtl_ot_num = Column(Integer, nullable=False)
    dtl_oc_num = Column(Integer, nullable=True)
    line_num = Column(Integer, nullable=False)
    dtl_id = Column(Integer, nullable=False)
    detail_utc = Column(DateTime, nullable=False)
    detail_lcl = Column(DateTime, nullable=False)
    last_update_utc = Column(DateTime, nullable=False)
    last_update_lcl = Column(DateTime, nullable=False)
    bus_dt = Column(String, nullable=False)
    ws_num = Column(Integer, nullable=False)
    dsp_ttl = Column(Float, nullable=False)
    dsp_qty = Column(Integer, nullable=False)
    agg_ttl = Column(Float, nullable=False)
    agg_qty = Column(Integer, nullable=False)
    chk_emp_id = Column(Integer, nullable=False)
    chk_emp_num = Column(Integer, nullable=False)
    svc_rnd_num = Column(Integer, nullable=False)
    seat_num = Column(Integer, nullable=False)
    guest_check_id = Column(Integer, ForeignKey('guest_checks.guest_check_id'))

    # Relações
    menu_item = relationship("MenuItem", back_populates="detail_line")
    guest_check = relationship("GuestCheck", back_populates="detail_lines")

# Tabela de Menu Items
class MenuItem(Base):
    __tablename__ = 'menu_items'

    mi_num = Column(Integer, primary_key=True)
    mod_flag = Column(Boolean, nullable=False)
    incl_tax = Column(Float, nullable=False)
    active_taxes = Column(String, nullable=False)
    prc_lvl = Column(Integer, nullable=False)
    detail_line_id = Column(Integer, ForeignKey('detail_lines.guest_check_line_item_id'))

    # Relação inversa
    detail_line = relationship("DetailLine", back_populates="menu_item")

# Exemplo de engine e criação do banco de dados
engine = create_engine("sqlite:///restaurant.db")
Base.metadata.create_all(engine)

# Sessão para interações
Session = sessionmaker(bind=engine)
session = Session()