...
@Table({ tableName: 'fridge_user' })
export class fridge_user extends Model<fridge_user> {
  @PrimaryKey
  @Column
  login: string;

  @Column
  password: string;

  @BeforeCreate
  @BeforeUpdate
  static async hashPassword(user: fridge_user) {
    user.password = await hash(user.password, 10);
  }

  @HasMany(() => fridge_user_device_relation)
  fridge_user_device_relation: fridge_user_device_relation[];

  @HasMany(() => shopping_list)
  shopping_list: shopping_list[];
}